# EMA Hourly Continuation — FLOKI/USDT P8_100

**Symbol:** FLOKI/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 681 |
| net_profit_factor | 0.6735 |
| net_win_rate | 0.4772 |
| gross_profit_factor | 0.9705 |
| gross_win_rate | 0.4860 |
| sharpe_ratio | -3.6871 |
| sortino_ratio | -1.3514 |
| max_drawdown | 0.8135 |
| cagr | -0.4760 |
| net_avg_win | 50.9419 |
| net_avg_loss | -69.0528 |
| avg_hold_time_bars | 21.4523 |
| exposure | 0.6640 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
