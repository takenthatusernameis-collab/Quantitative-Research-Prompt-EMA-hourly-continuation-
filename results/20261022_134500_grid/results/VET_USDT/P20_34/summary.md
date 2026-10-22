# EMA Hourly Continuation — VET/USDT P20_34

**Symbol:** VET/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1123 |
| net_profit_factor | 0.3864 |
| net_win_rate | 0.4292 |
| gross_profit_factor | 0.9251 |
| gross_win_rate | 0.4639 |
| sharpe_ratio | -10.6476 |
| sortino_ratio | -5.0656 |
| max_drawdown | 0.9987 |
| cagr | -0.9285 |
| net_avg_win | 13.0470 |
| net_avg_loss | -25.3906 |
| avg_hold_time_bars | 2.6411 |
| exposure | 0.1348 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
