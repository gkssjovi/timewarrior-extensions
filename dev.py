#!/usr/bin/env python3

import time
import os
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler
import shutil

abs_dest = os.path.expanduser('~/.timewarrior/extensions')
src = './src'
abs_src = os.path.abspath(src)

if __name__ == '__main__':
    patterns = ['*']
    ignore_patterns = None
    ignore_directories = False
    case_sensitive = True
    event_handler = PatternMatchingEventHandler(patterns, ignore_patterns, ignore_directories, case_sensitive)

    def watch(event):
        src_path = event.src_path
        is_directory = event.is_directory
        event_type = event.event_type
        
        if src_path == abs_src:
            return None
        
        src_path_rel = os.path.relpath(src_path, src)
        dest = os.path.join(abs_dest, src_path_rel)
        
        try:
            if event_type == 'deleted':
                if os.path.exists(dest) and not is_directory:
                    os.remove(dest)
                    print(f'{event_type}: {dest}')
            else:
                shutil.copyfile(src_path, dest)
                print(f'{event_type}: {dest}')
        except OSError as e:
            print(str(e))
        
    event_handler.on_created = watch
    event_handler.on_deleted = watch
    event_handler.on_modified = watch
    event_handler.on_moved = watch
    
    go_recursively = True
    observer = Observer()
    observer.schedule(event_handler, src, recursive=go_recursively)
    
    observer.start()
    
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
        observer.join()
