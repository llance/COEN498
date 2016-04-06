// grid.ts
import {Component} from 'angular2/core';
import {Column} from './column';
import {Sorter} from './sorter';


@Component({
    selector: 'grid',
    inputs: ['rows: rows', 'columns: columns'],
    templateUrl: './src/library/grid.html'
})

export class Grid {
    columns: Array<Column>;
    rows: Array<any>;
    sorter: Sorter;
    constructor() {
        this.sorter = new Sorter();
    }
    // sort(key) {
    //     this.sorter.sort(key, this.rows);
    // }
}
