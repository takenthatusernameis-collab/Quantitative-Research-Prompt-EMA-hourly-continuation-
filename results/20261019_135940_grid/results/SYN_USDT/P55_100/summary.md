# EMA Hourly Continuation — SYN/USDT P55_100

**Symbol:** SYN/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 626 |
| net_profit_factor | 0.5964 |
| net_win_rate | 0.4681 |
| gross_profit_factor | 0.9949 |
| gross_win_rate | 0.4824 |
| sharpe_ratio | -4.3914 |
| sortino_ratio | -1.5522 |
| max_drawdown | 0.8481 |
| cagr | -0.5238 |
| net_avg_win | 42.6114 |
| net_avg_loss | -62.8637 |
| avg_hold_time_bars | 6.1565 |
| exposure | 0.1752 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
