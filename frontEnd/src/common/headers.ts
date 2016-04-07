import { Headers } from 'angular2/http';

export const contentHeaders = new Headers();
contentHeaders.append('Accept', 'application/json');
contentHeaders.append('Content-Type', 'application/x-www-form-urlencoded');
contentHeaders.append('WWW-Authenticate', localStorage.getItem('jwt'));

