# ISS-Info
<!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->
[![All Contributors](https://img.shields.io/badge/all_contributors-2-orange.svg?style=flat-square)](#contributors-)
[![MIT license](https://img.shields.io/badge/License-MIT-blue.svg)](https://lbesson.mit-license.org/)
<!-- ALL-CONTRIBUTORS-BADGE:END -->
 
Python wrapper for tracking information about International Space Station via http://open-notify.org

## Installation

In order install this package, simply run:

```bash
pip install ISS_Info
```

## Usage

To use ISS_Info, you first need to import the package:

```python
import ISS_Info
```

### International Space Station Current Location:

```python
ISS_Info.iss_current_loc()     # Returns a dictionary with latitude, longitude, timestamp.
```

### How Many People Are In ISS Right Now:

```python
ISS_Info.iss_people_in_space()     # Returns a dictionary with number, names, craft information.
```

### International Space Station Pass Times:
Given a location on Earth (latitude, longitude, and altitude) this API will compute the next n number of times that the ISS will be overhead. Overhead is defined as 10° in elevation for the observer. The times are computed in UTC and the length of time that the ISS is above 10° is in seconds.

```python
ISS_Info.iss_passes(43.5,-74,200,3)     # Returns a dictionary with every pass information.
```
|  Input  |  Description  |  Parameter Name  |  Valid Range  |  Units  |  Required  |
|---------|---------------|------------------|---------------|---------|------------|
|Latitude | The latitude of the place to predict passes              |      lat            |     -80 ~ 80          |   degrees      | YES |
|   Longitude      |   	The longitude of the place to predict passes             |    lon              |     -180 ~ 180          |   degrees      | YES |
|   Altitude      |    The altitude of the place to predict passes           |           alt       |      0 ~ 10,000         |         meters| Optional |
|Number|The number of passes to return|n|1 ~ 100|–| Optional|

## Contributors ✨

Thanks goes to these wonderful people ([emoji key](https://allcontributors.org/docs/en/emoji-key)):

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tr>
    <td align="center"><a href="https://github.com/salil-gtm"><img src="https://avatars2.githubusercontent.com/u/18382251?v=4" width="100px;" alt=""/><br /><sub><b>Salil Gautam</b></sub></a><br /><a href="https://github.com/Quarantine-Projects/ISS_Info/commits?author=salil-gtm" title="Code">💻</a> <a href="https://github.com/Quarantine-Projects/ISS_Info/commits?author=salil-gtm" title="Documentation">📖</a> <a href="#example-salil-gtm" title="Examples">💡</a></td>
    <td align="center"><a href="https://github.com/pdx97"><img src="https://avatars3.githubusercontent.com/u/28250686?v=4" width="100px;" alt=""/><br /><sub><b>Pdx97</b></sub></a><br /><a href="https://github.com/Quarantine-Projects/ISS_Info/commits?author=pdx97" title="Code">💻</a> <a href="https://github.com/Quarantine-Projects/ISS_Info/commits?author=pdx97" title="Documentation">📖</a> <a href="#example-pdx97" title="Examples">💡</a></td>
  </tr>
</table>

<!-- markdownlint-enable -->
<!-- prettier-ignore-end -->
<!-- ALL-CONTRIBUTORS-LIST:END -->

This project follows the [all-contributors](https://github.com/all-contributors/all-contributors) specification. Contributions of any kind welcome!
