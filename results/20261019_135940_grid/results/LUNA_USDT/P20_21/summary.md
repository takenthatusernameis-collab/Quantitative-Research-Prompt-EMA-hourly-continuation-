# EMA Hourly Continuation — LUNA/USDT P20_21

**Symbol:** LUNA/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1323 |
| net_profit_factor | 0.1535 |
| net_win_rate | 0.2623 |
| gross_profit_factor | 0.7027 |
| gross_win_rate | 0.3477 |
| sharpe_ratio | -20.3034 |
| sortino_ratio | -11.5630 |
| max_drawdown | 1.0000 |
| cagr | -0.9987 |
| net_avg_win | 5.2263 |
| net_avg_loss | -12.1040 |
| avg_hold_time_bars | 1.6296 |
| exposure | 0.0980 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
