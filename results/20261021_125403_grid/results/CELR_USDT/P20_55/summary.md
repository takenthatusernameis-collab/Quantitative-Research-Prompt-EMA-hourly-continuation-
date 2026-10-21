# EMA Hourly Continuation — CELR/USDT P20_55

**Symbol:** CELR/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 609 |
| net_profit_factor | 0.7048 |
| net_win_rate | 0.4778 |
| gross_profit_factor | 0.9438 |
| gross_win_rate | 0.4778 |
| sharpe_ratio | -3.0225 |
| sortino_ratio | -1.0634 |
| max_drawdown | 0.7242 |
| cagr | -0.3856 |
| net_avg_win | 58.0492 |
| net_avg_loss | -75.3659 |
| avg_hold_time_bars | 9.0411 |
| exposure | 0.2492 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
