// library.ts
import { Component, View } from 'angular2/core';
import { CORE_DIRECTIVES, NgForm, ControlGroup } from 'angular2/common';
import { Http, Headers } from 'angular2/http';
import { Router } from 'angular2/router';
import { contentHeaders } from '../common/headers';
import { FormBuilder, Validators } from 'angular2/common';
// import { Grid } from './grid';
// import { Column } from './column';

let styles = require('./library.css');
let template = require('./library.html');


@Component({
    selector: 'library',
    // directives: [CORE_DIRECTIVES], //Grid
    // // template: '<grid name="person grid" [rows]="people" [columns]="columns"></grid>',
    // styles: [styles]
})


@View({
    directives: [CORE_DIRECTIVES],
            template: template,
            styles: [styles]
        })

export class Library {
    BookInJson;

    // people: Array<Person>;
    // columns: Array<Column>;

    // getPeople(): Array<Person> {
    //     return [
    //         { title: 'Joe', authors: 'Jackson', subtitle: 20 },
    //     ];
    // }

    // getColumns(): Array<Column> {
    //     return [
    //         new Column('title', 'Title'),
    //         new Column('authors', 'Authors'),
    //         new Column('subtitle', 'Subtitle'),
    //         new Column('pageCount', 'Page Count'),
    //         new Column('publisher', 'Publisher'),
    //         new Column('publishedDate', 'Published Date'),
    //         new Column('language', 'Language'),
    //     ];
    // }

    constructor(public router: Router, public http: Http) {
        // this.people = this.getPeople();
        // this.columns = this.getColumns();
    }

    viewBooks() {
        event.preventDefault();
        contentHeaders.append('X-CSRFToken', this.getCookie('csrftoken'));
        this.http.get('http://localhost:8000/books/', { headers: contentHeaders })
            .subscribe(
            response => {
                var jsonResponse = response.json();
                console.log('response received!', jsonResponse);
                this.BookInJson = jsonResponse;
            },
            error => {
                alert(error.text());
                console.log(error.text());
            }
            );
    }

    getCookie(name) {
        console.log('document.cookie is ', document.cookie);
        let value = '; ' + document.cookie;
        let parts = value.split('; ' + name + '=');
        if (parts.length === 2)
            return parts.pop().split(';').shift();
    }
}

// interface Person {
//     firstName: string;
//     lastName: string;
//     age: number;
// }
