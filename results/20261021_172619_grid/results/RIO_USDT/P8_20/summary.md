# EMA Hourly Continuation — RIO/USDT P8_20

**Symbol:** RIO/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 407 |
| net_profit_factor | 0.7742 |
| net_win_rate | 0.4742 |
| gross_profit_factor | 0.9309 |
| gross_win_rate | 0.4742 |
| sharpe_ratio | -1.8351 |
| sortino_ratio | -0.5298 |
| max_drawdown | 0.4809 |
| cagr | -0.2172 |
| net_avg_win | 81.0087 |
| net_avg_loss | -94.3693 |
| avg_hold_time_bars | 5.8108 |
| exposure | 0.1086 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
