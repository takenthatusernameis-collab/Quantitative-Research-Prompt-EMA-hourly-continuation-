# EMA Hourly Continuation — CATI/USDT P21_34

**Symbol:** CATI/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 267 |
| net_profit_factor | 0.6191 |
| net_win_rate | 0.4569 |
| gross_profit_factor | 0.8240 |
| gross_win_rate | 0.4569 |
| sharpe_ratio | -2.6546 |
| sortino_ratio | -0.6782 |
| max_drawdown | 0.4889 |
| cagr | -0.2696 |
| net_avg_win | 63.9866 |
| net_avg_loss | -86.9544 |
| avg_hold_time_bars | 5.4569 |
| exposure | 0.0799 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
