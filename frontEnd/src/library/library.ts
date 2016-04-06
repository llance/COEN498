// library.ts
import { Component, View } from 'angular2/core';
import { CORE_DIRECTIVES, NgForm, ControlGroup } from 'angular2/common';
import { Http, Headers } from 'angular2/http';
import { Router } from 'angular2/router';
import { contentHeaders } from '../common/headers';
import { FormBuilder, Validators } from 'angular2/common';
import { bootstrap } from 'angular2/platform/browser';
import { Http, HTTP_PROVIDERS } from 'angular2/http';

let styles = require('./library.css');
let template = require('./library.html');

bootstrap(Library, [HTTP_PROVIDERS]);

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

    viewBooks() {
        console.log('viewBooks called');
        event.preventDefault();
        this.http.get('http://localhost:8000/books/', { headers: contentHeaders })
            .subscribe(
            response => {
                var jsonResponse = response.json();
                console.log('response received!', jsonResponse);
                // this.router.parent.navigateByUrl('/home');
            },
            error => {
                alert(error.text());
                console.log(error.text());
            }
            );
    }
}
