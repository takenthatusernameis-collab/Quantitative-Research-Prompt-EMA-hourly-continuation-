# EMA Hourly Continuation — OGN/USDT P8_100

**Symbol:** OGN/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 597 |
| net_profit_factor | 0.5768 |
| net_win_rate | 0.4539 |
| gross_profit_factor | 0.9031 |
| gross_win_rate | 0.4657 |
| sharpe_ratio | -4.3329 |
| sortino_ratio | -1.4733 |
| max_drawdown | 0.8438 |
| cagr | -0.5110 |
| net_avg_win | 42.0202 |
| net_avg_loss | -60.5599 |
| avg_hold_time_bars | 25.6231 |
| exposure | 0.6922 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
