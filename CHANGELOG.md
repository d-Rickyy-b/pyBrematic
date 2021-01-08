# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/), and this project adheres
to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [1.2.1] - 2021-01-09
### Fixed
- Fixed wrong attribute name leading to `AttributeError: 'CMR500' object has no attribute 'baud'` ([#21](https://github.com/d-Rickyy-b/pyBrematic/issues/21))

## [1.2.0] - 2021-01-05
### Added

- Implement CMR300, CMR500 and ITR300 devices ([1a9082a](https://github.com/d-Rickyy-b/pyBrematic/commit/1a9082a67e5c025c2dd7e0b8d2fc47108df204c6), [740ecf1](https://github.com/d-Rickyy-b/pyBrematic/commit/82ff04c5f69b778ea27f8f105f54d9fae43b03ce), [82ff04c](https://github.com/d-Rickyy-b/pyBrematic/commit/82ff04c5f69b778ea27f8f105f54d9fae43b03ce))
- Add methods to generate system and unit code for intertechno devices ([380ba42](https://github.com/d-Rickyy-b/pyBrematic/commit/380ba42d3d811c1aee74b93c83e74c88402b27c8))
- Implement ConnAir gateway ([40ac9e9](https://github.com/d-Rickyy-b/pyBrematic/commit/40ac9e90e998c55a74a4f7ad2688bda97ba92d66))

## [1.1.0] - 2020-12-27

### Added

- Implement support for ITR3500 ([3fc05b1](https://github.com/d-Rickyy-b/pyBrematic/commit/3fc05b1c9683c72dd1291dbb353f30bed3e040dd))
- Support for local storage needed for autopair ([ca29013](https://github.com/d-Rickyy-b/pyBrematic/commit/ca29013edd693855628231d05f0ef9c6aac8f4c8))
- Implement Intertechno autopair devices such as ITL500 ([0fd8123](https://github.com/d-Rickyy-b/pyBrematic/commit/0fd812356d573c7cd332c75071c3f53e5e8f59e1))
- Add Action enum to easily choose the action that should be executed ([c983641](https://github.com/d-Rickyy-b/pyBrematic/commit/c98364196b69230c6a8dd48c9d805ebfdf66f97e))

### CI

- Implement GitHub Actions workflow for building and deploying packages on each release (PS: might still be a bit buggy at the moment)

## [1.0.0] - 2018-07-07

### Added

- Implemented Intertechno gateway ([cb13362](https://github.com/d-Rickyy-b/pyBrematic/commit/cb1336296e82e0dbb34c0abb5f9fe4a7f2bf3c4f))
- Implement CMR1000 and PAR1500 ([40427d9](https://github.com/d-Rickyy-b/pyBrematic/commit/40427d9d70abb94832a62715ab885103f1a8b20a))
- Implement AB440SA ([7d61f49](https://github.com/d-Rickyy-b/pyBrematic/commit/7d61f49214938118486d3c20d52b489d2585e148))

### Fixed

- Fix get_signal function for RCR1000N device ([90001d7](https://github.com/d-Rickyy-b/pyBrematic/commit/90001d7bd62c15cca066343b8b649ea1f465daa7))

## [0.0.1] - 2018-05-10

Initial release with a single gateway and outlet.

[unreleased]: https://github.com/d-Rickyy-b/pyBrematic/compare/v1.2.1...HEAD
[1.2.1]: https://github.com/d-Rickyy-b/pyBrematic/compare/v1.2.0...v1.2.1
[1.2.0]: https://github.com/d-Rickyy-b/pyBrematic/compare/v1.1.0...v1.2.0
[1.1.0]: https://github.com/d-Rickyy-b/pyBrematic/compare/v1.0.0...v1.1.0
[1.0.0]: https://github.com/d-Rickyy-b/pyBrematic/compare/v0.0.1...v1.0.0
[0.0.1]: https://github.com/d-Rickyy-b/pyBrematic/tree/v0.0.1
