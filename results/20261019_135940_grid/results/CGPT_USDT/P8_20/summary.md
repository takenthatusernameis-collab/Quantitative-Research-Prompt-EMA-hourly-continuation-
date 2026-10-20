# EMA Hourly Continuation — CGPT/USDT P8_20

**Symbol:** CGPT/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1645 |
| net_profit_factor | 0.4281 |
| net_win_rate | 0.4359 |
| gross_profit_factor | 0.9731 |
| gross_win_rate | 0.4565 |
| sharpe_ratio | -11.3920 |
| sortino_ratio | -6.4819 |
| max_drawdown | 0.9998 |
| cagr | -0.9634 |
| net_avg_win | 10.4377 |
| net_avg_loss | -18.8377 |
| avg_hold_time_bars | 2.8255 |
| exposure | 0.2113 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
