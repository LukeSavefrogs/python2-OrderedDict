# OrderedDictionary
Backporting of the `OrderedDict` class from the `collection` package that can be used in **legacy Python 2** scripts (_tested on Python 2.1_).


## Roadmap
- [X] Implement `.clear()`
- [X] Implement `.copy()`
- [ ] Implement `.get()`
- [ ] Implement `.update()`
- [ ] Implement `.setdefault()`
- [ ] Implement `.pop()`
- [ ] Implement `.popitem()`
- [ ] Implement `.move_to_end(key, last)`
- [ ] Implement `.fromkeys(keylist, value)`


## Special thanks
The [**original version**](https://github.com/amina196/OrderedDictionary) was uploaded by [@Amina Bouabdallah](https://github.com/amina196) on **May 26, 2012** 
(_11 years ago at the moment of writing_).

I just blew the dust off the repo, adjusted the code to work on Jython 2.1 and added some features.