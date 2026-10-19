# EMA Hourly Continuation — HBAR/USDT P20_21

**Symbol:** HBAR/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1230 |
| net_profit_factor | 0.1102 |
| net_win_rate | 0.2935 |
| gross_profit_factor | 0.6236 |
| gross_win_rate | 0.3707 |
| sharpe_ratio | -18.9115 |
| sortino_ratio | -10.3613 |
| max_drawdown | 1.0000 |
| cagr | -0.9972 |
| net_avg_win | 3.4290 |
| net_avg_loss | -12.9319 |
| avg_hold_time_bars | 1.5398 |
| exposure | 0.0861 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
