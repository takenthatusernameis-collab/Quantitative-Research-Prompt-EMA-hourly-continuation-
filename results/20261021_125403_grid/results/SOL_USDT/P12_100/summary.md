# EMA Hourly Continuation — SOL/USDT P12_100

**Symbol:** SOL/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 486 |
| net_profit_factor | 0.7705 |
| net_win_rate | 0.4918 |
| gross_profit_factor | 0.9809 |
| gross_win_rate | 0.4918 |
| sharpe_ratio | -1.9666 |
| sortino_ratio | -0.6195 |
| max_drawdown | 0.5374 |
| cagr | -0.2485 |
| net_avg_win | 71.9370 |
| net_avg_loss | -90.3362 |
| avg_hold_time_bars | 22.9280 |
| exposure | 0.5065 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
