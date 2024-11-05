import { Component } from '@angular/core';
import { WikiSearchService } from './wiki-search.service';

@Component({
  selector: 'app-wiki-search',
  templateUrl: './wiki-search.component.html',
  styleUrls: ['./wiki-search.component.css']
})
export class WikiSearchComponent {
  query: string = '';
  mood: string = 'General';
  results: any[] = [];
  showScoreInfo: boolean = true; 

  constructor(private wikiSearchService: WikiSearchService) {}

  toggleShowScoreInfo () {
    this.showScoreInfo = !this.showScoreInfo;
  }

  onSearch(): void {
    if (this.query) {
      console.log('query = ' + this.query);
      this.wikiSearchService.searchArticles(this.query, this.mood)
        .subscribe((response) => {
          this.results = response.results;
        });
    }
  }
}
