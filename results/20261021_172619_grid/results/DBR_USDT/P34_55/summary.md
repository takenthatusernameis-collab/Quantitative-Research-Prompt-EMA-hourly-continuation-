# EMA Hourly Continuation — DBR/USDT P34_55

**Symbol:** DBR/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 250 |
| net_profit_factor | 0.4888 |
| net_win_rate | 0.4480 |
| gross_profit_factor | 0.8211 |
| gross_win_rate | 0.4520 |
| sharpe_ratio | -3.8384 |
| sortino_ratio | -0.9665 |
| max_drawdown | 0.6035 |
| cagr | -0.3648 |
| net_avg_win | 51.0376 |
| net_avg_loss | -84.7493 |
| avg_hold_time_bars | 8.8080 |
| exposure | 0.1252 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
