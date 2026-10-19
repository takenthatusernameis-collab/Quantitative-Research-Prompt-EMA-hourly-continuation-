# EMA Hourly Continuation — HBAR/USDT P89_100

**Symbol:** HBAR/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 631 |
| net_profit_factor | 0.2250 |
| net_win_rate | 0.3629 |
| gross_profit_factor | 0.6914 |
| gross_win_rate | 0.4120 |
| sharpe_ratio | -10.4813 |
| sortino_ratio | -3.8611 |
| max_drawdown | 0.9947 |
| cagr | -0.8740 |
| net_avg_win | 12.6047 |
| net_avg_loss | -31.9189 |
| avg_hold_time_bars | 2.0935 |
| exposure | 0.0600 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
