# EMA Hourly Continuation — ORDI/USDT P26_89

**Symbol:** ORDI/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 738 |
| net_profit_factor | 0.6153 |
| net_win_rate | 0.4607 |
| gross_profit_factor | 0.8918 |
| gross_win_rate | 0.4634 |
| sharpe_ratio | -4.7048 |
| sortino_ratio | -1.7967 |
| max_drawdown | 0.8913 |
| cagr | -0.5770 |
| net_avg_win | 41.6211 |
| net_avg_loss | -57.7859 |
| avg_hold_time_bars | 8.4566 |
| exposure | 0.2837 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
