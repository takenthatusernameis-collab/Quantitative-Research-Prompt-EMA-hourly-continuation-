# EMA Hourly Continuation — CHZ/USDT P50_100

**Symbol:** CHZ/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 598 |
| net_profit_factor | 0.5516 |
| net_win_rate | 0.4783 |
| gross_profit_factor | 1.0228 |
| gross_win_rate | 0.5017 |
| sharpe_ratio | -4.5803 |
| sortino_ratio | -1.5962 |
| max_drawdown | 0.8534 |
| cagr | -0.5304 |
| net_avg_win | 36.5610 |
| net_avg_loss | -60.7622 |
| avg_hold_time_bars | 6.2592 |
| exposure | 0.1701 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
