# EMA Hourly Continuation — NYM/USDT P12_100

**Symbol:** NYM/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 371 |
| net_profit_factor | 0.5737 |
| net_win_rate | 0.4394 |
| gross_profit_factor | 0.7882 |
| gross_win_rate | 0.4420 |
| sharpe_ratio | -3.2844 |
| sortino_ratio | -0.8960 |
| max_drawdown | 0.6614 |
| cagr | -0.3379 |
| net_avg_win | 53.2513 |
| net_avg_loss | -72.7404 |
| avg_hold_time_bars | 34.5553 |
| exposure | 0.5827 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
