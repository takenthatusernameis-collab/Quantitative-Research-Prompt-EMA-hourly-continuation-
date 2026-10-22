# EMA Hourly Continuation — DOT/USDT P8_20

**Symbol:** DOT/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1736 |
| net_profit_factor | 0.2730 |
| net_win_rate | 0.4263 |
| gross_profit_factor | 0.8243 |
| gross_win_rate | 0.4539 |
| sharpe_ratio | -13.5048 |
| sortino_ratio | -7.9791 |
| max_drawdown | 1.0000 |
| cagr | -0.9834 |
| net_avg_win | 5.0739 |
| net_avg_loss | -13.8096 |
| avg_hold_time_bars | 2.6809 |
| exposure | 0.2115 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
