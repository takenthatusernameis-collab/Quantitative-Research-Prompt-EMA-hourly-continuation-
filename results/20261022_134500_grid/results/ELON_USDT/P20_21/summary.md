# EMA Hourly Continuation — ELON/USDT P20_21

**Symbol:** ELON/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 908 |
| net_profit_factor | 0.1338 |
| net_win_rate | 0.3084 |
| gross_profit_factor | 0.4943 |
| gross_win_rate | 0.3469 |
| sharpe_ratio | -14.5367 |
| sortino_ratio | -6.5244 |
| max_drawdown | 0.9999 |
| cagr | -0.9721 |
| net_avg_win | 5.5150 |
| net_avg_loss | -18.3805 |
| avg_hold_time_bars | 2.1454 |
| exposure | 0.0885 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
