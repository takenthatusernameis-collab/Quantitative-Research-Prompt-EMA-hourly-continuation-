# EMA Hourly Continuation — CTC/USDT P55_89

**Symbol:** CTC/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 309 |
| net_profit_factor | 0.5186 |
| net_win_rate | 0.4369 |
| gross_profit_factor | 0.7626 |
| gross_win_rate | 0.4369 |
| sharpe_ratio | -3.4839 |
| sortino_ratio | -0.8738 |
| max_drawdown | 0.6452 |
| cagr | -0.3333 |
| net_avg_win | 50.9645 |
| net_avg_loss | -76.2492 |
| avg_hold_time_bars | 7.7379 |
| exposure | 0.1087 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
