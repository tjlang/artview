ARTview
=======

ARM Radar Toolkit Viewer

ARTview is an interactive viewing browser that uses the PyArt toolkit.  
It allows one to easily scroll through a directory of weather radar data files 
and visualize the data.  All file types available in PyArt can be opened with
the ARTview browser.

With ARTview you can:

	Dynamically switch fields (variables) and tilt angles via drop down menu.
    
    Dynamically switch tilt angle by button selection.
    
    Browse a directory by advancing with drop down "Next" and "Previous" menus or by arrow key.
    
    View ground-based or airborne radar.
    
    View PPI, sector or RHI type files
    
  
## Installation
Currently it is a standalone executable python script, but may eventually be wrapped into PyArt after maturation.
No specific installation is required, outside of PyArt dependency.

## Usage

```python
python artview.py /some/directory/you/want/to/point/to
```

The file can also be made executable by
```python
chmod +x artview.py
```

Then it can be run by calling :
```python
artview.py /some/directory/you/want/to/point/to
```

To see the command line options:
```python
artview.py -h
```

To plot an RHI formatted file, you can use the --rhi flag:
```python
artview.py --rhi /some/directory/with/RHI/files
```

To plot airborne sweep data, you can use the --airborne flag:
```python
artview.py --airborne /some/directory/with/airbrone/sweep/files
```

ARTview should be able to recognize RHI and airborne files, though this has not
been robustly tested to date.

The default startup uses radar reflectivity and checks for a few common names.
If you find a file with a field that does not load, let me know and I can add it
to the list.

## Dependencies
[Py-Art](https://github.com/ARM-DOE/pyart)

[matplotlib](http://matplotlib.org)

[TkInter](https://wiki.python.org/moin/TkInter)

Developed on Python 2.7.7 :: Anaconda 2.0.1 
MacOSX 10.9.4

Author: Nick Guy (nick.guy@noaa.gov)

NOTE:: This is open source software.  Contributions are very welcome, though this is not my primary project.  In addition it needs to be state that no responsibility is taken by the author for any adverse effects.

At the current time the scaling and limit changing fields are very slow.
