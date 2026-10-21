# EMA Hourly Continuation — NYM/USDT P8_21

**Symbol:** NYM/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 518 |
| net_profit_factor | 0.3916 |
| net_win_rate | 0.4498 |
| gross_profit_factor | 0.7859 |
| gross_win_rate | 0.4556 |
| sharpe_ratio | -5.3383 |
| sortino_ratio | -1.7361 |
| max_drawdown | 0.8730 |
| cagr | -0.5579 |
| net_avg_win | 24.0642 |
| net_avg_loss | -50.2428 |
| avg_hold_time_bars | 10.4344 |
| exposure | 0.2457 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
