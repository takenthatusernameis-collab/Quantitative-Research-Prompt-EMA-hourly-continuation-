# EMA Hourly Continuation — KAVA/USDT P8_89

**Symbol:** KAVA/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 774 |
| net_profit_factor | 0.6078 |
| net_win_rate | 0.4509 |
| gross_profit_factor | 1.0340 |
| gross_win_rate | 0.4767 |
| sharpe_ratio | -5.7911 |
| sortino_ratio | -2.2446 |
| max_drawdown | 0.9435 |
| cagr | -0.6736 |
| net_avg_win | 41.7363 |
| net_avg_loss | -56.3881 |
| avg_hold_time_bars | 18.6189 |
| exposure | 0.6550 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
