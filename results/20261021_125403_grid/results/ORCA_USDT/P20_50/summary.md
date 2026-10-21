# EMA Hourly Continuation — ORCA/USDT P20_50

**Symbol:** ORCA/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 572 |
| net_profit_factor | 0.7439 |
| net_win_rate | 0.5035 |
| gross_profit_factor | 1.0292 |
| gross_win_rate | 0.5035 |
| sharpe_ratio | -2.4346 |
| sortino_ratio | -0.8336 |
| max_drawdown | 0.6510 |
| cagr | -0.3195 |
| net_avg_win | 62.4826 |
| net_avg_loss | -85.1813 |
| avg_hold_time_bars | 8.0594 |
| exposure | 0.2095 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
