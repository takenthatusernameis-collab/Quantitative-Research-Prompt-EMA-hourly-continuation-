# EMA Hourly Continuation — KMNO/USDT P21_200

**Symbol:** KMNO/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 377 |
| net_profit_factor | 0.6019 |
| net_win_rate | 0.4403 |
| gross_profit_factor | 0.8341 |
| gross_win_rate | 0.4509 |
| sharpe_ratio | -3.3092 |
| sortino_ratio | -0.9010 |
| max_drawdown | 0.6694 |
| cagr | -0.3559 |
| net_avg_win | 60.3944 |
| net_avg_loss | -78.9346 |
| avg_hold_time_bars | 33.9151 |
| exposure | 0.5903 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
