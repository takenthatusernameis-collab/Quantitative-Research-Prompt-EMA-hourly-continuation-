# EMA Hourly Continuation — POL/USDT P50_144

**Symbol:** POL/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 524 |
| net_profit_factor | 0.4911 |
| net_win_rate | 0.4695 |
| gross_profit_factor | 0.8108 |
| gross_win_rate | 0.4790 |
| sharpe_ratio | -4.1527 |
| sortino_ratio | -1.3320 |
| max_drawdown | 0.8150 |
| cagr | -0.4793 |
| net_avg_win | 31.6089 |
| net_avg_loss | -56.9554 |
| avg_hold_time_bars | 12.2538 |
| exposure | 0.2919 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
