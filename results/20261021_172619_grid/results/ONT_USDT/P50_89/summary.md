# EMA Hourly Continuation — ONT/USDT P50_89

**Symbol:** ONT/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 380 |
| net_profit_factor | 0.6516 |
| net_win_rate | 0.4789 |
| gross_profit_factor | 0.8986 |
| gross_win_rate | 0.4789 |
| sharpe_ratio | -2.4873 |
| sortino_ratio | -0.6916 |
| max_drawdown | 0.5752 |
| cagr | -0.2718 |
| net_avg_win | 56.5906 |
| net_avg_loss | -79.8341 |
| avg_hold_time_bars | 8.2237 |
| exposure | 0.1414 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
