# EMA Hourly Continuation — SEI/USDT P12_21

**Symbol:** SEI/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 292 |
| net_profit_factor | 0.6675 |
| net_win_rate | 0.4692 |
| gross_profit_factor | 0.9131 |
| gross_win_rate | 0.4692 |
| sharpe_ratio | -2.3837 |
| sortino_ratio | -0.5823 |
| max_drawdown | 0.5240 |
| cagr | -0.2344 |
| net_avg_win | 71.6287 |
| net_avg_loss | -94.8431 |
| avg_hold_time_bars | 5.0000 |
| exposure | 0.0664 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
