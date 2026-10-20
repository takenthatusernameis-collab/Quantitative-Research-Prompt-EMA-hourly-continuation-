# EMA Hourly Continuation — KAVA/USDT P20_34

**Symbol:** KAVA/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1207 |
| net_profit_factor | 0.3460 |
| net_win_rate | 0.3803 |
| gross_profit_factor | 0.8327 |
| gross_win_rate | 0.4283 |
| sharpe_ratio | -13.1768 |
| sortino_ratio | -6.5765 |
| max_drawdown | 0.9998 |
| cagr | -0.9684 |
| net_avg_win | 11.5255 |
| net_avg_loss | -20.4392 |
| avg_hold_time_bars | 3.4176 |
| exposure | 0.1875 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
