# EMA Hourly Continuation — OGN/USDT P8_26

**Symbol:** OGN/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 808 |
| net_profit_factor | 0.6844 |
| net_win_rate | 0.4851 |
| gross_profit_factor | 0.9747 |
| gross_win_rate | 0.4864 |
| sharpe_ratio | -3.8672 |
| sortino_ratio | -1.5707 |
| max_drawdown | 0.8477 |
| cagr | -0.5136 |
| net_avg_win | 46.3463 |
| net_avg_loss | -63.8086 |
| avg_hold_time_bars | 6.6559 |
| exposure | 0.2434 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
