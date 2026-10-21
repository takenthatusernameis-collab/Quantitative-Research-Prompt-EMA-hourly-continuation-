# EMA Hourly Continuation — XTZ/USDT P26_100

**Symbol:** XTZ/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 483 |
| net_profit_factor | 0.7738 |
| net_win_rate | 0.5052 |
| gross_profit_factor | 1.0357 |
| gross_win_rate | 0.5052 |
| sharpe_ratio | -1.8774 |
| sortino_ratio | -0.5926 |
| max_drawdown | 0.5122 |
| cagr | -0.2382 |
| net_avg_win | 69.4166 |
| net_avg_loss | -91.5810 |
| avg_hold_time_bars | 16.1284 |
| exposure | 0.3541 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
