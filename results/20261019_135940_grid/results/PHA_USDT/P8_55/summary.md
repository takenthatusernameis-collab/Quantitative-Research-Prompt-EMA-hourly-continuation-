# EMA Hourly Continuation — PHA/USDT P8_55

**Symbol:** PHA/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1047 |
| net_profit_factor | 0.5826 |
| net_win_rate | 0.4670 |
| gross_profit_factor | 0.9135 |
| gross_win_rate | 0.4737 |
| sharpe_ratio | -5.3926 |
| sortino_ratio | -2.4382 |
| max_drawdown | 0.9497 |
| cagr | -0.6948 |
| net_avg_win | 27.0924 |
| net_avg_loss | -40.7538 |
| avg_hold_time_bars | 10.0926 |
| exposure | 0.4803 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
