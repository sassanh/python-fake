# Changelog

## Version 0.1.3

- refactor: improve iteration behavior in `__iter__`, `__next__`, `__aiter__` and `__anext__` methods
- test: add tests for iteration behavior

## Version 0.1.2

- fix: revert making `Fake` a subclass of `Coroutine` as it conflicts with `__next__` and `__await__` behavior

## Version 0.1.1

- feat: make `Fake` a subclass of `Coroutine`
- feat: make `__file` customizable
- refactor: rename `props` to `attrs` to be aligned with python conventions
- test: add tests for core functionality

## Version 0.1.0

- feat: implementation of the `Fake` class

## Version 0.0.0
