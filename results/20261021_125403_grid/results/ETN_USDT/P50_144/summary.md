# EMA Hourly Continuation — ETN/USDT P50_144

**Symbol:** ETN/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 304 |
| net_profit_factor | 0.6465 |
| net_win_rate | 0.4539 |
| gross_profit_factor | 0.8049 |
| gross_win_rate | 0.4539 |
| sharpe_ratio | -2.4457 |
| sortino_ratio | -0.6614 |
| max_drawdown | 0.5014 |
| cagr | -0.2631 |
| net_avg_win | 62.7646 |
| net_avg_loss | -80.7040 |
| avg_hold_time_bars | 13.6842 |
| exposure | 0.2260 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
