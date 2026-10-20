# EMA Hourly Continuation — BOME/USDT P26_144

**Symbol:** BOME/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 460 |
| net_profit_factor | 0.6623 |
| net_win_rate | 0.4870 |
| gross_profit_factor | 0.8932 |
| gross_win_rate | 0.4891 |
| sharpe_ratio | -2.2995 |
| sortino_ratio | -0.6972 |
| max_drawdown | 0.6062 |
| cagr | -0.2805 |
| net_avg_win | 49.2515 |
| net_avg_loss | -70.5834 |
| avg_hold_time_bars | 23.0826 |
| exposure | 0.4826 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
