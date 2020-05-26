class Manager():
    script_list = [
        ('sample', 'sample'),
        ('sample2', 'sample2')
    ]

    @staticmethod
    def invoke(script, file):
        '''
            To invoke the selected script
        '''
        from importlib import import_module
        module = import_module(f'app.script_mgmt.scripts.{script}')

        return module.main(file)

    @staticmethod
    def save(output, filename):
        '''
            To handle different file formats
        '''
        format = filename.split('.')[-1]
        if format == 'xml':
            output.write(filename)
        elif format in ['csv', 'xlsx']:
            if format == 'xlsx':
                filename = filename.replace('.xlsx', '.csv')
            output.to_csv(filename, index = False)

        return filename

    # @staticmethod
    # def delete(filename):
    #     from os import remove
    #     remove(filename)
