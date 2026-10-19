# EMA Hourly Continuation — OP/USDT P8_12

**Symbol:** OP/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1824 |
| net_profit_factor | 0.1712 |
| net_win_rate | 0.3635 |
| gross_profit_factor | 0.5992 |
| gross_win_rate | 0.4062 |
| sharpe_ratio | -17.6163 |
| sortino_ratio | -10.8651 |
| max_drawdown | 1.0000 |
| cagr | -0.9969 |
| net_avg_win | 3.1158 |
| net_avg_loss | -10.3926 |
| avg_hold_time_bars | 1.7626 |
| exposure | 0.1461 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
