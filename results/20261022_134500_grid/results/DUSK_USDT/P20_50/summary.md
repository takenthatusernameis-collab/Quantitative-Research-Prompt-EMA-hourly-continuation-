# EMA Hourly Continuation — DUSK/USDT P20_50

**Symbol:** DUSK/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 958 |
| net_profit_factor | 0.5997 |
| net_win_rate | 0.4374 |
| gross_profit_factor | 1.0032 |
| gross_win_rate | 0.4509 |
| sharpe_ratio | -6.6816 |
| sortino_ratio | -2.9119 |
| max_drawdown | 0.9730 |
| cagr | -0.7533 |
| net_avg_win | 34.6925 |
| net_avg_loss | -44.9698 |
| avg_hold_time_bars | 4.7119 |
| exposure | 0.2052 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
