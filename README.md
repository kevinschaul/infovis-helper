# InfoVis helper functions - Get your data in line
By Kevin Schaul - @foxyNinja7

Here are some python functions (only one as of now) to help get data in the correct json format for use with the JavaScript InfoVis Toolkit, by Nicolas Garcia Belmonte.

http://thejit.org/

### Treemaps

## createLevel(name, id, area, color, children=[], data={})

* Takes in the label of the square, a unique id, integer size area, hex color, optional list of children, and optional dict of extra data.
* Returns a dict which can later be put into a list and converted to json.


## Release notes

### 8/22/2011
* Initial release

## License

The MIT License

Copyright (c) 2011 Kevin Schaul

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.