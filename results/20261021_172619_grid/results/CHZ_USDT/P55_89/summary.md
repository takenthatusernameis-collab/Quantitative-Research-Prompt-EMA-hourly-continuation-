# EMA Hourly Continuation — CHZ/USDT P55_89

**Symbol:** CHZ/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 301 |
| net_profit_factor | 0.8248 |
| net_win_rate | 0.5382 |
| gross_profit_factor | 1.1682 |
| gross_win_rate | 0.5415 |
| sharpe_ratio | -1.0056 |
| sortino_ratio | -0.2522 |
| max_drawdown | 0.2918 |
| cagr | -0.1102 |
| net_avg_win | 73.8562 |
| net_avg_loss | -104.3661 |
| avg_hold_time_bars | 6.4153 |
| exposure | 0.0878 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
