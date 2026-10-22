# EMA Hourly Continuation — MOCA/USDT P21_26

**Symbol:** MOCA/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 196 |
| net_profit_factor | 0.6062 |
| net_win_rate | 0.4796 |
| gross_profit_factor | 0.9150 |
| gross_win_rate | 0.4796 |
| sharpe_ratio | -2.2371 |
| sortino_ratio | -0.4714 |
| max_drawdown | 0.4205 |
| cagr | -0.1931 |
| net_avg_win | 63.3071 |
| net_avg_loss | -96.2382 |
| avg_hold_time_bars | 4.5459 |
| exposure | 0.0447 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
