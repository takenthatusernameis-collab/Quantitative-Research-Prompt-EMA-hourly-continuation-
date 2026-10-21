# EMA Hourly Continuation — TRAC/USDT P8_21

**Symbol:** TRAC/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 566 |
| net_profit_factor | 0.6744 |
| net_win_rate | 0.4647 |
| gross_profit_factor | 0.9302 |
| gross_win_rate | 0.4647 |
| sharpe_ratio | -3.4556 |
| sortino_ratio | -1.1725 |
| max_drawdown | 0.7569 |
| cagr | -0.4162 |
| net_avg_win | 58.3687 |
| net_avg_loss | -75.1232 |
| avg_hold_time_bars | 7.3074 |
| exposure | 0.1880 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
