# EMA Hourly Continuation — SLP/USDT P12_21

**Symbol:** SLP/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 433 |
| net_profit_factor | 0.6932 |
| net_win_rate | 0.4942 |
| gross_profit_factor | 0.9953 |
| gross_win_rate | 0.4942 |
| sharpe_ratio | -2.5555 |
| sortino_ratio | -0.7643 |
| max_drawdown | 0.5939 |
| cagr | -0.2942 |
| net_avg_win | 61.5634 |
| net_avg_loss | -86.7850 |
| avg_hold_time_bars | 4.8383 |
| exposure | 0.0952 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
