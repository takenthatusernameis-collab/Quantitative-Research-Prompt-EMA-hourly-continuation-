# EMA Hourly Continuation — BDX/USDT P8_21

**Symbol:** BDX/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 317 |
| net_profit_factor | 0.3273 |
| net_win_rate | 0.3186 |
| gross_profit_factor | 0.5492 |
| gross_win_rate | 0.3218 |
| sharpe_ratio | -6.5492 |
| sortino_ratio | -1.6807 |
| max_drawdown | 0.8642 |
| cagr | -0.5484 |
| net_avg_win | 41.6363 |
| net_avg_loss | -59.4777 |
| avg_hold_time_bars | 4.5047 |
| exposure | 0.0649 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
