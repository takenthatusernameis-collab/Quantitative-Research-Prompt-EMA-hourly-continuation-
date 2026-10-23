# EMA Hourly Continuation — FLUX/USDT P21_34

**Symbol:** FLUX/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1123 |
| net_profit_factor | 0.3672 |
| net_win_rate | 0.4372 |
| gross_profit_factor | 0.8634 |
| gross_win_rate | 0.4630 |
| sharpe_ratio | -9.9747 |
| sortino_ratio | -4.7579 |
| max_drawdown | 0.9976 |
| cagr | -0.9085 |
| net_avg_win | 11.7891 |
| net_avg_loss | -24.9427 |
| avg_hold_time_bars | 2.3704 |
| exposure | 0.1210 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
