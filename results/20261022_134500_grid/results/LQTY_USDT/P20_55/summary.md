# EMA Hourly Continuation — LQTY/USDT P20_55

**Symbol:** LQTY/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 937 |
| net_profit_factor | 0.5226 |
| net_win_rate | 0.4610 |
| gross_profit_factor | 0.8758 |
| gross_win_rate | 0.4707 |
| sharpe_ratio | -5.8791 |
| sortino_ratio | -2.5317 |
| max_drawdown | 0.9538 |
| cagr | -0.7030 |
| net_avg_win | 24.1563 |
| net_avg_loss | -39.5399 |
| avg_hold_time_bars | 6.9146 |
| exposure | 0.2932 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
