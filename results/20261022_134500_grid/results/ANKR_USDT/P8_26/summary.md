# EMA Hourly Continuation — ANKR/USDT P8_26

**Symbol:** ANKR/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1536 |
| net_profit_factor | 0.3907 |
| net_win_rate | 0.4134 |
| gross_profit_factor | 0.8232 |
| gross_win_rate | 0.4395 |
| sharpe_ratio | -12.0059 |
| sortino_ratio | -6.6548 |
| max_drawdown | 0.9998 |
| cagr | -0.9647 |
| net_avg_win | 10.0960 |
| net_avg_loss | -18.2116 |
| avg_hold_time_bars | 4.2220 |
| exposure | 0.2948 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
