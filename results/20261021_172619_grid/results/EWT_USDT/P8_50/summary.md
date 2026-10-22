# EMA Hourly Continuation — EWT/USDT P8_50

**Symbol:** EWT/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 621 |
| net_profit_factor | 0.6047 |
| net_win_rate | 0.4316 |
| gross_profit_factor | 0.7554 |
| gross_win_rate | 0.4316 |
| sharpe_ratio | -3.9019 |
| sortino_ratio | -1.3751 |
| max_drawdown | 0.7973 |
| cagr | -0.4691 |
| net_avg_win | 45.4470 |
| net_avg_loss | -57.0557 |
| avg_hold_time_bars | 11.8792 |
| exposure | 0.3353 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
