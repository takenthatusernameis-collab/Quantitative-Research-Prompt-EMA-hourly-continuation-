# EMA Hourly Continuation — ALGO/USDT P21_200

**Symbol:** ALGO/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 303 |
| net_profit_factor | 0.8770 |
| net_win_rate | 0.5116 |
| gross_profit_factor | 1.0357 |
| gross_win_rate | 0.5116 |
| sharpe_ratio | -0.6883 |
| sortino_ratio | -0.1717 |
| max_drawdown | 0.2550 |
| cagr | -0.0784 |
| net_avg_win | 85.2830 |
| net_avg_loss | -101.8484 |
| avg_hold_time_bars | 44.2145 |
| exposure | 0.6090 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
