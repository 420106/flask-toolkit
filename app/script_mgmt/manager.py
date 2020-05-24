class Manager():
    script_list = [
        ('sample', 'sample'),
        ('sample2', 'sample2')
    ]
    temp_files = 'app\\script_mgmt\\temp\\'

    @staticmethod
    def invoke(script, file):
        from importlib import import_module
        module = import_module(f'app.script_mgmt.scripts.{script}')

        return module.main(file)

    def save(self, output, filename):
        '''
            To handle write functions of different package used in the scripts
        '''
        format = filename.split('.')[-1]
        if format == 'xml':
            output.write(filename)
        elif format == 'csv':
            output.to_csv(filename)
