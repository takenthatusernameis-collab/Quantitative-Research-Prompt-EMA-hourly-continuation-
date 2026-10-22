# EMA Hourly Continuation — DOGE/USDT P21_144

**Symbol:** DOGE/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 438 |
| net_profit_factor | 0.5385 |
| net_win_rate | 0.4361 |
| gross_profit_factor | 0.8549 |
| gross_win_rate | 0.4589 |
| sharpe_ratio | -4.4003 |
| sortino_ratio | -1.2798 |
| max_drawdown | 0.8034 |
| cagr | -0.4698 |
| net_avg_win | 48.6712 |
| net_avg_loss | -69.8932 |
| avg_hold_time_bars | 28.2100 |
| exposure | 0.5616 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
