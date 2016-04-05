import {Component, View} from 'angular2/core';

@Component({
  selector: 'front-end'
})

@View({
  templateUrl: 'front-end.html'
})

export class FrontEnd {

  constructor() {
    console.info('FrontEnd Component Mounted Successfully');
  }

}
