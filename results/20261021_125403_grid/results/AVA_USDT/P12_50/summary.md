# EMA Hourly Continuation — AVA/USDT P12_50

**Symbol:** AVA/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 619 |
| net_profit_factor | 0.7644 |
| net_win_rate | 0.5008 |
| gross_profit_factor | 0.9939 |
| gross_win_rate | 0.5008 |
| sharpe_ratio | -2.0948 |
| sortino_ratio | -0.7475 |
| max_drawdown | 0.6084 |
| cagr | -0.2901 |
| net_avg_win | 60.3699 |
| net_avg_loss | -79.2376 |
| avg_hold_time_bars | 9.6607 |
| exposure | 0.2718 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
