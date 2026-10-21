# EMA Hourly Continuation — ORCA/USDT P8_21

**Symbol:** ORCA/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 718 |
| net_profit_factor | 0.7160 |
| net_win_rate | 0.5042 |
| gross_profit_factor | 1.0335 |
| gross_win_rate | 0.5070 |
| sharpe_ratio | -2.9656 |
| sortino_ratio | -1.1402 |
| max_drawdown | 0.7637 |
| cagr | -0.4077 |
| net_avg_win | 50.9494 |
| net_avg_loss | -72.3577 |
| avg_hold_time_bars | 5.8231 |
| exposure | 0.1900 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
