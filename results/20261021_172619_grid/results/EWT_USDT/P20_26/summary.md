# EMA Hourly Continuation — EWT/USDT P20_26

**Symbol:** EWT/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 168 |
| net_profit_factor | 0.5477 |
| net_win_rate | 0.4345 |
| gross_profit_factor | 0.7531 |
| gross_win_rate | 0.4345 |
| sharpe_ratio | -2.3546 |
| sortino_ratio | -0.4335 |
| max_drawdown | 0.4021 |
| cagr | -0.1819 |
| net_avg_win | 65.6913 |
| net_avg_loss | -92.1678 |
| avg_hold_time_bars | 7.7202 |
| exposure | 0.0590 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
