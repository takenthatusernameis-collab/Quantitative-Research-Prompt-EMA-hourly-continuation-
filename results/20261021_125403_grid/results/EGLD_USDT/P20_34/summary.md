# EMA Hourly Continuation — EGLD/USDT P20_34

**Symbol:** EGLD/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 358 |
| net_profit_factor | 0.6635 |
| net_win_rate | 0.4888 |
| gross_profit_factor | 0.9678 |
| gross_win_rate | 0.4888 |
| sharpe_ratio | -2.4880 |
| sortino_ratio | -0.6761 |
| max_drawdown | 0.5554 |
| cagr | -0.2656 |
| net_avg_win | 60.7694 |
| net_avg_loss | -87.5895 |
| avg_hold_time_bars | 4.8212 |
| exposure | 0.0785 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
