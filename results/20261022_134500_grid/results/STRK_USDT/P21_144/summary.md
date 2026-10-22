# EMA Hourly Continuation — STRK/USDT P21_144

**Symbol:** STRK/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 508 |
| net_profit_factor | 0.7095 |
| net_win_rate | 0.4803 |
| gross_profit_factor | 0.9638 |
| gross_win_rate | 0.4843 |
| sharpe_ratio | -2.7707 |
| sortino_ratio | -0.8748 |
| max_drawdown | 0.6972 |
| cagr | -0.3433 |
| net_avg_win | 65.2781 |
| net_avg_loss | -85.0354 |
| avg_hold_time_bars | 22.0256 |
| exposure | 0.5086 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
