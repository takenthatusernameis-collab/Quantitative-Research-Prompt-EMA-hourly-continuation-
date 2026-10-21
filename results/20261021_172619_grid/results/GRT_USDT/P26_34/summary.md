# EMA Hourly Continuation — GRT/USDT P26_34

**Symbol:** GRT/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 168 |
| net_profit_factor | 0.5850 |
| net_win_rate | 0.4524 |
| gross_profit_factor | 0.8263 |
| gross_win_rate | 0.4524 |
| sharpe_ratio | -2.1568 |
| sortino_ratio | -0.3986 |
| max_drawdown | 0.3765 |
| cagr | -0.1669 |
| net_avg_win | 68.4611 |
| net_avg_loss | -96.6750 |
| avg_hold_time_bars | 4.3155 |
| exposure | 0.0328 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
