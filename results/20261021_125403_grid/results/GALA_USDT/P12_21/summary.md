# EMA Hourly Continuation — GALA/USDT P12_21

**Symbol:** GALA/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 292 |
| net_profit_factor | 0.6334 |
| net_win_rate | 0.4623 |
| gross_profit_factor | 0.8621 |
| gross_win_rate | 0.4623 |
| sharpe_ratio | -2.4806 |
| sortino_ratio | -0.6054 |
| max_drawdown | 0.5191 |
| cagr | -0.2431 |
| net_avg_win | 64.4046 |
| net_avg_loss | -87.4319 |
| avg_hold_time_bars | 4.9075 |
| exposure | 0.0651 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
