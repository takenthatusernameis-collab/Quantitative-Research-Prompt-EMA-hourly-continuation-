# EMA Hourly Continuation — CELR/USDT P12_26

**Symbol:** CELR/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1362 |
| net_profit_factor | 0.3840 |
| net_win_rate | 0.4192 |
| gross_profit_factor | 0.8146 |
| gross_win_rate | 0.4391 |
| sharpe_ratio | -10.3982 |
| sortino_ratio | -5.4364 |
| max_drawdown | 0.9988 |
| cagr | -0.9294 |
| net_avg_win | 10.9049 |
| net_avg_loss | -20.4984 |
| avg_hold_time_bars | 3.4589 |
| exposure | 0.2132 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
