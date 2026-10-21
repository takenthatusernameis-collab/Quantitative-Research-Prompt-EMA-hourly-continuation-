# EMA Hourly Continuation — CTC/USDT P20_26

**Symbol:** CTC/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 256 |
| net_profit_factor | 0.6628 |
| net_win_rate | 0.5078 |
| gross_profit_factor | 1.0217 |
| gross_win_rate | 0.5117 |
| sharpe_ratio | -1.8892 |
| sortino_ratio | -0.4352 |
| max_drawdown | 0.3974 |
| cagr | -0.1796 |
| net_avg_win | 59.2370 |
| net_avg_loss | -92.2054 |
| avg_hold_time_bars | 5.8867 |
| exposure | 0.0685 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
