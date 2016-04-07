// library.ts
import { Component, View } from 'angular2/core';
import { CORE_DIRECTIVES, NgForm, ControlGroup } from 'angular2/common';
import { Http, Headers } from 'angular2/http';
import { Router } from 'angular2/router';
import { contentHeaders } from '../common/headers';
import { FormBuilder, Validators } from 'angular2/common';
import { Column } from './column';

//let styles = require('./library.css');
//let template = require('./library.html');


@Component({
    selector: 'library',
    inputs: ['item: item', 'columns: columns'],
    templateUrl: './src/library/library.html',
    // styleUrls: ['./src/library/library.css']
})

export class Library {
    BookInJson;
    type;

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
             new Column('artists', 'Artists'),
             new Column('numDisks', '# of Disks'),
             new Column('physicalMedium', 'Physical Medium'),
             new Column('label', 'Label'),
         ];
     }

    constructor(public router: Router, public http: Http) {
         this.columns = this.getColumnsBooks();
    }

    viewBooks() {
        event.preventDefault();
        this.type = 'book';
        console.log('token is ', localStorage.getItem('jwt'));
        contentHeaders.append('WWW-Authenticate', localStorage.getItem('jwt'));
        //contentHeaders.append('X-CSRFToken', this.getCookie('csrftoken'));
        this.http.get('http://localhost:8000/books/', { headers: contentHeaders })
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
        this.type = 'movie';
        contentHeaders.append('WWW-Authenticate', localStorage.getItem('jwt'));
        this.http.get('http://localhost:8000/movies/', { headers: contentHeaders })
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
        this.type = 'music';
        console.log('token is ', localStorage.getItem('jwt'));
        contentHeaders.append('WWW-Authenticate', localStorage.getItem('jwt'));
        //contentHeaders.append('X-CSRFToken', this.getCookie('csrftoken'));
        this.http.get('http://localhost:8000/musics/', { headers: contentHeaders })
            .subscribe(
            response => {
                var jsonResponse = response.json();
                console.log('response received!', jsonResponse);
                console.log('string response', JSON.stringify(jsonResponse));
                this.columns = this.getColumnsMusic();
                console.log(jsonResponse);
                this.item = jsonResponse;
            },
            error => {
                alert(error.text());
                console.log(error.text());
            });
    }

    viewHome() {
        this.router.parent.navigateByUrl('/home');
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
        var message = 'deleted ';

        for (var i = 1; i < table.rows.length; i++) {
            var row: HTMLTableObject = table.rows[i];
            var chkbox = document.getElementsByName('chkbox');
            var inner: HTMLInputElement = <HTMLInputElement> chkbox[i-1];

            if (inner.checked) {
            isbn_upc = row.cells[0].innerHTML;
            console.log('deleting', isbn_upc);
            message = message + isbn_upc + ' ';
            var data = "{\"item_type\": \"" + this.type + "\",\"unique_id\": \"" + isbn_upc + "\"}";
            console.log(data);
            this.sendDelete(data);
            }
        }
        alert(message);
        switch (this.type) {
            case 'book': this.viewBooks(); return;
            case 'movie': this.viewMovies(); return;
            case 'music': this.viewMusic(); return;
        }
    }

    sendDelete(data_string) {
        contentHeaders.append('WWW-Authenticate', localStorage.getItem('jwt'));
        console.log(data_string);
        var url = 'http://localhost:8000/' + this.type + 's/';
        this.http.delete(url, { headers: contentHeaders, body: data_string })
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

    logout() {
        localStorage.removeItem('jwttoken');
        localStorage.removeItem('restsessiontoken');
        this.router.parent.navigateByUrl('/login');
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
    artists: string;
    numDisks: string;
    physicalMedium: string;
    label: string;
}

