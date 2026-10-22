# EMA Hourly Continuation — MLK/USDT P50_89

**Symbol:** MLK/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 309 |
| net_profit_factor | 0.3271 |
| net_win_rate | 0.3139 |
| gross_profit_factor | 0.4943 |
| gross_win_rate | 0.3204 |
| sharpe_ratio | -5.9658 |
| sortino_ratio | -1.4914 |
| max_drawdown | 0.8360 |
| cagr | -0.5047 |
| net_avg_win | 41.5932 |
| net_avg_loss | -58.1849 |
| avg_hold_time_bars | 8.6246 |
| exposure | 0.1206 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
