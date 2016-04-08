// headerchecker.ts
import { contentHeaders } from '../common/headers';


export function HeaderChecker() {
    console.log('contentHeaders is : ', contentHeaders);

    if (contentHeaders.get('Authorization').indexOf('null') < 0){
        console.log('no jwt token in contentHeader, adding it...');
        contentHeaders.append('Authorization', 'Bearer ' + localStorage.getItem('jwttoken'));
    }
}