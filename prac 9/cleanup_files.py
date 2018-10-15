"""
CP1404/CP5632 Practical
Demos of various os module examples
"""
import shutil
import os


def main():
    """Demo os module functions."""
    print("Starting directory is: {}".format(os.getcwd()))

    os.chdir('F:\CP1404pracs\prac 9\Lyrics\Lyrics\Christmas')

    print("Files in {}:\n{}\n".format(os.getcwd(), os.listdir('.')))

    try:
        os.mkdir('temp')
    except FileExistsError:
        pass



        for filename in os.listdir('.'):
            if os.path.isdir(filename):
                continue

        new_name = get_fixed_filename(filename)
        print("Renaming {} to {}".format(filename, new_name))

        # Option 1: rename file to new name - in place
        #os.rename(filename, new_name)


        # Option 2: move file to new place, with new name
        shutil.move(filename, 'temp/' + new_name)


def get_fixed_filename(filename):
    """Return a 'fixed' version of filename."""
    new_name = filename.replace(" ", "_").replace(".TXT", ".txt")
    return new_name


def demo_walk():
    """Process all subdirectories using os.walk()."""
    os.chdir('F:\CP1404pracs\prac 9\Lyrics\Lyrics')
    for directory_name, subdirectories, filenames in os.walk('.'):
        print("Directory:", directory_name)
        print("\tcontains subdirectories:", subdirectories)
        print("\tand files:", filenames)
        print("(Current working directory is: {})".format(os.getcwd()))
        for filename in os.rename('F:\CP1404pracs\prac 9\Lyrics', 'F:\CP1404pracs\prac 9\Lyrics'):
            get_fixed_filename(filename)





 #main()
demo_walk()