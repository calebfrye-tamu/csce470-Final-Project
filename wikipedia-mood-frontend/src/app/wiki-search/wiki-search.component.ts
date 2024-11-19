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
  sortResultsBy: string = 'mood_weighted_score';

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
          this.sortResults();
        });
    }
  }

  setSort(sortBy: string) {
    this.sortResultsBy = sortBy;
    this.sortResults();
  }

  sortResults(): void {
    switch (this.sortResultsBy) {
      case 'mood_weighted_score':
        console.log("Sorting results by mood-weighted bm25 score");
        this.results = this.results.sort((a, b) => b.mood_weighted_score - a.mood_weighted_score);
        break;
      case 'raw_score':
        console.log("Sorting results by raw bm25 score");
        this.results = this.results.sort((a, b) => b.raw_score - a.raw_score);
        break;
      case 'mood_score':
        console.log("Sorting results by mood multiplier");
        this.results = this.results.sort((a, b) => b.mood_score - a.mood_score);
        break;
      default:
        break;
    }
  }

}
