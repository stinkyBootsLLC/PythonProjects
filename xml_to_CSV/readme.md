# STIG Checklist Value Extractor

> Purpose: To extract certain attribute values from 
the [STIG VIEWER](https://public.cyber.mil/stigs/srg-stig-tools/) .ckl file for reports 
> I wanted to extract specific values from the STIG Viewer application checklist file, 
to use for creating reports. 
 

| V-id     | Severity |         Title          | Status      |     Detail      |      Comment         |
| ---------| ---------| -----------------------| ------------| ----------------|  --------------------|
| V-123456 | low      | Title of vulnerability | NotAFinding |settings not set | working on a solution!


 
## Getting Started

These instructions will get you a copy of the project up and running on your local machine 
for development and testing purposes.  

- Download this repository to your local machine. The XML (.ckl) file must be in the same directory
as the (.py) file.
- Run the .py file from local directory and follow instructions 
on the console.
- the extension of the file DOES NOT MATTER as long as the file is a properly XML formatted file.
- The input file will have the .ckl extension.
- The output file name can be anything you want - I like .txt to keep it simple
- Note:".ckl" must follow the same tree structure as "example.ckl" in this repository
- Once the program is complete, use Excel to IMPORT the newly created file. (The one you named)
- Once the program is complete, use Excel (or any other spreadsheet program) to IMPORT the newly created file. 
(The one you named)
- Use the (|) character as the delimiter.

### Prerequisites

Must have Python 3.8 installed on host machine.

```
Give examples
```

### Installing

A step by step series of examples that tell you how to get a development env running

Say what the step will be

```
Give the example
```

And repeat

```
until finished
```

End with an example of getting some data out of the system or using it for a little demo

## Running the tests

Explain how to run the automated tests for this system

### Break down into end to end tests

Explain what these tests test and why

```
Give an example
```

### And coding style tests

Explain what these tests test and why

```
Give an example
```

## Deployment

Add additional notes about how to deploy this on a live system

## Built With

* [Dropwizard](http://www.dropwizard.io/1.0.2/docs/) - The web framework used
* [Maven](https://maven.apache.org/) - Dependency Management
* [ROME](https://rometools.github.io/rome/) - Used to generate RSS Feeds

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

## Authors

* **Billie Thompson** - *Initial work* - [PurpleBooth](https://github.com/PurpleBooth)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration
* etc
