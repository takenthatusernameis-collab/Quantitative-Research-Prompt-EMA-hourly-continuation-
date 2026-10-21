# EMA Hourly Continuation — JASMY/USDT P50_55

**Symbol:** JASMY/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 85 |
| net_profit_factor | 0.6818 |
| net_win_rate | 0.4824 |
| gross_profit_factor | 0.9286 |
| gross_win_rate | 0.4824 |
| sharpe_ratio | -1.0931 |
| sortino_ratio | -0.1443 |
| max_drawdown | 0.1555 |
| cagr | -0.0639 |
| net_avg_win | 79.8831 |
| net_avg_loss | -109.1823 |
| avg_hold_time_bars | 5.2706 |
| exposure | 0.0204 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
