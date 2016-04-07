// library.ts
import { Component, View } from 'angular2/core';
import { CORE_DIRECTIVES, NgForm, ControlGroup } from 'angular2/common';
import { Http, Headers } from 'angular2/http';
import { Router } from 'angular2/router';
import { contentHeaders } from '../common/headers';
import { FormBuilder, Validators } from 'angular2/common';
import { Column } from './column';

let styles = require('./library.css');
let template = require('./library.html');


@Component({
    selector: 'library',
    inputs: ['item: item', 'columns: columns'],
    templateUrl: './src/library/library.html'
})

export class Library {
    BookInJson;

     item: Array<any>;
     columns: Array<Column>;

     getColumnsBooks(): Array<Column> {
         return [
             new Column('isbn', 'isbn'),
             new Column('title', 'Title'),
             new Column('authors', 'Authors'),
             new Column('subtitle', 'Subtitle'),
             new Column('pageCount', 'Pages'),
             new Column('publisher', 'Publisher'),
             new Column('publishedDate', 'Published Date'),
             new Column('language', 'Language'),
         ];
     }

    getColumnsMovies(): Array<Column> {
         return [
             new Column('upc', 'upc'),
             new Column('title', 'Title'),
             new Column('directors', 'Directors'),
             new Column('subtitle', 'Subtitle'),
             new Column('length', 'Length'),
             new Column('publisher', 'Publisher'),
             new Column('productFormat', 'Product Format'),
             new Column('language', 'Language'),
         ];
     }

    getColumnsMusic(): Array<Column> {
         return [
             new Column('upc', 'upc'),
             new Column('title', 'Title'),
             new Column('artist', 'Artist'),
             new Column('album', 'Album'),
             new Column('length', 'Length'),
             new Column('publisher', 'Publisher'),
             new Column('publishedDate', 'Published Date'),
             new Column('language', 'Language'),
         ];
     }

    constructor(public router: Router, public http: Http) {
         this.columns = this.getColumnsBooks();
    }

    viewBooks() {
        event.preventDefault();
        console.log('token is ', localStorage.getItem('jwt'));
        contentHeaders.append('WWW-Authenticate', localStorage.getItem('jwt'));
        //contentHeaders.append('X-CSRFToken', this.getCookie('csrftoken'));
        this.http.get('http://localhost:8000/getbooks/', { headers: contentHeaders })
            .subscribe(
            response => {
                var jsonResponse = response.json();
                console.log('response received!', jsonResponse);
                console.log('string response', JSON.stringify(jsonResponse));
                this.columns = this.getColumnsBooks();
                this.item = jsonResponse;
            },
            error => {
                alert(error.text());
                console.log(error.text());
            }
            );
    }

    viewMovies() {
        event.preventDefault();
        contentHeaders.append('WWW-Authenticate', localStorage.getItem('jwt'));
        this.http.get('http://localhost:8000/getmovies/', { headers: contentHeaders })
            .subscribe(
            response => {
                var jsonResponse = response.json();
                console.log('response received!', jsonResponse);
                console.log('string response', JSON.stringify(jsonResponse));
                this.columns = this.getColumnsMovies();
                this.item = jsonResponse;
            },
            error => {
                alert(error.text());
                console.log(error.text());
            });
    }

    viewMusic() {
        event.preventDefault();
        console.log('token is ', localStorage.getItem('jwt'));
        contentHeaders.append('WWW-Authenticate', localStorage.getItem('jwt'));
        //contentHeaders.append('X-CSRFToken', this.getCookie('csrftoken'));
        this.http.get('http://localhost:8000/music/', { headers: contentHeaders })
            .subscribe(
            response => {
                var jsonResponse = response.json();
                console.log('response received!', jsonResponse);
                console.log('string response', JSON.stringify(jsonResponse));
                this.columns = this.getColumnsMusic();
                this.item = jsonResponse();
            },
            error => {
                alert(error.text());
                console.log(error.text());
            });
    }

    getCookie(name) {
        console.log('document.cookie is ', document.cookie);
        let value = '; ' + document.cookie;
        let parts = value.split('; ' + name + '=');
        if (parts.length === 2)
            return parts.pop().split(';').shift();
    }

    delete() {
        console.log('delete clicked');
        event.preventDefault();
        var table: HTMLTableElement = <HTMLTableElement> document.getElementById('tbl');
        var isbn_upc = '';
        var type = (<HTMLTableObject> table.rows[0]).cells[0].innerHTML;
        for (var i = 1; i < table.rows.length; i++) {
            var row: HTMLTableObject = table.rows[i];
            var index = row.cells.length;
            var inner: HTMLInputElement = <HTMLInputElement> row.cells[index - 1].innerHTML;
                if (inner.indexOf('checked') >= 0) {    //TODO: fix since this is always true
                isbn_upc = row.cells[0].innerHTML;
                console.log('deleting', isbn_upc);
                //alert('will try to delete', isbn_upc)
                var data = "{\"item_type\": \"book\",\"unique_id\": \"" + isbn_upc + "\"}";

                //todo: call http delete
                this.sendDelete(data);
                }
        }
    }

    sendDelete(data_string) {
        contentHeaders.append('WWW-Authenticate', localStorage.getItem('jwt'));
        //contentHeaders.append('X-CSRFToken', this.getCookie('csrftoken'));
        console.log(data_string);
        this.http.delete('http://localhost:8000/library/', { headers: contentHeaders, body: data_string })
            .subscribe(
            response => {
                var jsonResponse = response.json();
                console.log('delete response received!', jsonResponse);
            },
            error => {
                alert(error.text());
                console.log(error.text());
            }
            );
    }
}

interface Book {
    title: string;
    authors: string;
    subtitle: string;
    pageCount: string;
    publisher: string;
    publishedDate: string;
    language: string;
}

interface Movie {
    title: string;
    directors: string;
    subtitle: string;
    length: string;
    publisher: string;
    publishedDate: string;
    language: string;
}

interface Music {
    title: string;
    artist: string;
    album: string;
    length: string;
    publisher: string;
    publishedDate: string;
    language: string;
}

