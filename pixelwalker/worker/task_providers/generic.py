# -*- coding: utf8 -*-
from celery.execute import send_task

import os
import json, requests
import subprocess
import uuid

class TaskProvider(object):
    """This class defines a processing task"""

    def __init__(self, task_id, input_file_path):
        """Task initialization
        
        :param task_id: The task identifier
        :type task_id: int
        :param input_file_path: The input video file path
        :type input_file_path: str
        """
        self.task_id = int(task_id)
        if os.path.isfile(input_file_path) is True:       
            self.input_file_path = input_file_path
            self.input_file_name = os.path.basename(input_file_path)
        else:
            raise ValueError('Cannot access the file: {}'.format(input_file_path))

        self.subprocess_pid = None
        self.subprocess_out = None
        self.subprocess_err = None

    def execute(self, command):
        """Launch a subprocess task
        :param command: Arguments array for the subprocess task
        :type command: str[]
        """
        proc = subprocess.Popen(command, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
        self.subprocess_pid = proc.pid
        
        self.acknowledge_processing()

        try:
            self.subprocess_out, self.subprocess_err = proc.communicate()
        except:
            self.acknowledge_error()

    def acknowledge_error(self):
        data = {}
        data['id'] = self.task_id
        data['state'] = 'ERROR'
        data['outputs'] = None
        self.acknowledge(data)
    
    def acknowledge_processing(self):
        data = {}
        data['id'] = self.task_id
        data['state'] = 'PROCESSING'
        data['outputs'] = None
        self.acknowledge(data)

    def acknowledge_success(self, data):
        data['id'] = self.task_id
        data['state'] = 'SUCCESS'
        self.acknowledge(data)

    def acknowledge(self, data):
        send_task('engine.tasks.acknowledge', args=[data])


    