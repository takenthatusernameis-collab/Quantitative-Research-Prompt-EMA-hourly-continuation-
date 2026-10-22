# EMA Hourly Continuation — CELR/USDT P26_50

**Symbol:** CELR/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 524 |
| net_profit_factor | 0.6673 |
| net_win_rate | 0.4733 |
| gross_profit_factor | 0.9303 |
| gross_win_rate | 0.4733 |
| sharpe_ratio | -3.1889 |
| sortino_ratio | -1.0420 |
| max_drawdown | 0.7143 |
| cagr | -0.3794 |
| net_avg_win | 56.5987 |
| net_avg_loss | -76.2117 |
| avg_hold_time_bars | 6.7767 |
| exposure | 0.1607 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
