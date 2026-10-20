# EMA Hourly Continuation — ROSE/USDT P12_50

**Symbol:** ROSE/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1093 |
| net_profit_factor | 0.6188 |
| net_win_rate | 0.4620 |
| gross_profit_factor | 0.9694 |
| gross_win_rate | 0.4703 |
| sharpe_ratio | -6.1675 |
| sortino_ratio | -2.8758 |
| max_drawdown | 0.9708 |
| cagr | -0.7472 |
| net_avg_win | 31.1339 |
| net_avg_loss | -43.2081 |
| avg_hold_time_bars | 7.3019 |
| exposure | 0.3628 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
