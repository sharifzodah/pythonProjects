
contents = ['This notice replaces any previously scheduled dates for the tickets',
            'Your not guilty plea is on file', 'Your hearing will be held in Manhattan']
filenames = ['doc.txt', 'report.txt', 'properties.txt']

for content, filename in zip(contents, filenames):
    f = open(f'../files/{filename}', 'w')
    f.write(content + '\n')
    f.close()
