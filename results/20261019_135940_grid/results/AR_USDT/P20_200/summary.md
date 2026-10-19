# EMA Hourly Continuation — AR/USDT P20_200

**Symbol:** AR/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 381 |
| net_profit_factor | 0.6712 |
| net_win_rate | 0.4698 |
| gross_profit_factor | 0.9046 |
| gross_win_rate | 0.4724 |
| sharpe_ratio | -2.5693 |
| sortino_ratio | -0.7023 |
| max_drawdown | 0.5772 |
| cagr | -0.2854 |
| net_avg_win | 64.9909 |
| net_avg_loss | -85.8086 |
| avg_hold_time_bars | 37.0919 |
| exposure | 0.6424 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
