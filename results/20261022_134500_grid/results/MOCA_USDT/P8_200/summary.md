# EMA Hourly Continuation — MOCA/USDT P8_200

**Symbol:** MOCA/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 353 |
| net_profit_factor | 0.6002 |
| net_win_rate | 0.4476 |
| gross_profit_factor | 0.8296 |
| gross_win_rate | 0.4504 |
| sharpe_ratio | -3.3313 |
| sortino_ratio | -0.9234 |
| max_drawdown | 0.6452 |
| cagr | -0.3566 |
| net_avg_win | 60.1945 |
| net_avg_loss | -81.2670 |
| avg_hold_time_bars | 44.4731 |
| exposure | 0.7870 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
