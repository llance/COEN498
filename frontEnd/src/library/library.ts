// library.ts
import { Component, View } from 'angular2/core';
import { CORE_DIRECTIVES, NgForm, ControlGroup } from 'angular2/common';
import { Http, Headers } from 'angular2/http';
import { Router } from 'angular2/router';
import { contentHeaders } from '../common/headers';
import { FormBuilder, Validators } from 'angular2/common';

let styles = require('./library.css');
let template = require('./library.html');



@Component({
    selector: 'library',
})

@View({
    directives: [CORE_DIRECTIVES],
    template: template,
    styles: [styles]
})
export class Library {

    constructor(public router: Router, public http: Http) {
    }

   
}