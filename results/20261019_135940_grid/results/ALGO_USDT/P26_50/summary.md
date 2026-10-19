# EMA Hourly Continuation — ALGO/USDT P26_50

**Symbol:** ALGO/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 940 |
| net_profit_factor | 0.4714 |
| net_win_rate | 0.4936 |
| gross_profit_factor | 0.9622 |
| gross_win_rate | 0.5138 |
| sharpe_ratio | -6.1799 |
| sortino_ratio | -2.6830 |
| max_drawdown | 0.9628 |
| cagr | -0.7267 |
| net_avg_win | 18.4777 |
| net_avg_loss | -38.2117 |
| avg_hold_time_bars | 3.3936 |
| exposure | 0.1450 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
