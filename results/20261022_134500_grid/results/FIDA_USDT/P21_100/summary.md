# EMA Hourly Continuation — FIDA/USDT P21_100

**Symbol:** FIDA/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 636 |
| net_profit_factor | 0.5402 |
| net_win_rate | 0.4560 |
| gross_profit_factor | 0.8340 |
| gross_win_rate | 0.4686 |
| sharpe_ratio | -4.2851 |
| sortino_ratio | -1.5173 |
| max_drawdown | 0.8478 |
| cagr | -0.5140 |
| net_avg_win | 33.9532 |
| net_avg_loss | -52.6780 |
| avg_hold_time_bars | 15.5739 |
| exposure | 0.4482 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
