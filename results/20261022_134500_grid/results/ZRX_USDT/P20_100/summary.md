# EMA Hourly Continuation — ZRX/USDT P20_100

**Symbol:** ZRX/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 636 |
| net_profit_factor | 0.6222 |
| net_win_rate | 0.4670 |
| gross_profit_factor | 0.9360 |
| gross_win_rate | 0.4748 |
| sharpe_ratio | -4.2187 |
| sortino_ratio | -1.4886 |
| max_drawdown | 0.8427 |
| cagr | -0.5146 |
| net_avg_win | 46.4250 |
| net_avg_loss | -65.3690 |
| avg_hold_time_bars | 14.9340 |
| exposure | 0.4317 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
