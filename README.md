# ShapeNetCoreMetadata

This is for Linux - but shouldnt be hard to modify for any other OS. 

The file rename.py takes all bottom level files in ShapeNetCore.v2 and renames them according to their actual names. 

1. Download ShapeNetCore.v2
2. Extract and cd into ShapeNetCore.v2 folder
3. clone this repository in that folder
4. Create file shapenet_models in your Downloads folder
4. Modify these lines in rename.py :
```python
directory = '~/Downloads/ShapeNetCore.v2/'
dest = os.path.join("~/Downloads/shapenet_models")
```
6. Download the metadata files from ShapeNet (you will find a few .csv files for the metadata that I have used already)
7. Paste special into a spreadsheet and make comma separated so (like the csv files here) 
8. Make sure that the names dont have any difficult to handle characters
9. Run with > python rename.py: This should rename all files and copy the obj and mtl across to the `/shapenet_models` folder
