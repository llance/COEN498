import {Component, View} from 'angular2/core';
import {bootstrap} from 'angular2/platform/browser';
import {FrontEnd} from 'front-end';

@Component({
  selector: 'main'
})

@View({
  directives: [FrontEnd],
  template: `
    <front-end></front-end>
  `
})

class Main {

}

bootstrap(Main);
