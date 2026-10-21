# EMA Hourly Continuation — MTL/USDT P12_100

**Symbol:** MTL/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 428 |
| net_profit_factor | 0.7933 |
| net_win_rate | 0.5047 |
| gross_profit_factor | 1.0394 |
| gross_win_rate | 0.5047 |
| sharpe_ratio | -1.7076 |
| sortino_ratio | -0.5043 |
| max_drawdown | 0.5209 |
| cagr | -0.2082 |
| net_avg_win | 79.0753 |
| net_avg_loss | -101.5612 |
| avg_hold_time_bars | 33.5397 |
| exposure | 0.6496 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
