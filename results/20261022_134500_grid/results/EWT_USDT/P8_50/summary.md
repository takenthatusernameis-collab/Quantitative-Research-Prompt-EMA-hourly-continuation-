# EMA Hourly Continuation — EWT/USDT P8_50

**Symbol:** EWT/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1087 |
| net_profit_factor | 0.4224 |
| net_win_rate | 0.4140 |
| gross_profit_factor | 0.7365 |
| gross_win_rate | 0.4259 |
| sharpe_ratio | -8.4812 |
| sortino_ratio | -3.9020 |
| max_drawdown | 0.9925 |
| cagr | -0.8571 |
| net_avg_win | 16.1263 |
| net_avg_loss | -26.9723 |
| avg_hold_time_bars | 7.6937 |
| exposure | 0.3801 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
