# EMA Hourly Continuation — MERL/USDT P21_50

**Symbol:** MERL/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 948 |
| net_profit_factor | 0.5698 |
| net_win_rate | 0.4589 |
| gross_profit_factor | 0.8550 |
| gross_win_rate | 0.4652 |
| sharpe_ratio | -5.4527 |
| sortino_ratio | -2.3689 |
| max_drawdown | 0.9449 |
| cagr | -0.6776 |
| net_avg_win | 28.6638 |
| net_avg_loss | -42.6543 |
| avg_hold_time_bars | 5.3439 |
| exposure | 0.2309 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
