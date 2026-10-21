# EMA Hourly Continuation — ETN/USDT P8_89

**Symbol:** ETN/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 511 |
| net_profit_factor | 0.5343 |
| net_win_rate | 0.3973 |
| gross_profit_factor | 0.6476 |
| gross_win_rate | 0.3973 |
| sharpe_ratio | -4.8004 |
| sortino_ratio | -1.6677 |
| max_drawdown | 0.8045 |
| cagr | -0.5384 |
| net_avg_win | 45.3840 |
| net_avg_loss | -55.9825 |
| avg_hold_time_bars | 18.0900 |
| exposure | 0.5021 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
