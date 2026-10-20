# EMA Hourly Continuation — MINA/USDT P20_55

**Symbol:** MINA/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 934 |
| net_profit_factor | 0.5903 |
| net_win_rate | 0.4754 |
| gross_profit_factor | 1.0099 |
| gross_win_rate | 0.4925 |
| sharpe_ratio | -5.5576 |
| sortino_ratio | -2.4035 |
| max_drawdown | 0.9473 |
| cagr | -0.6824 |
| net_avg_win | 30.6316 |
| net_avg_loss | -47.0193 |
| avg_hold_time_bars | 6.7741 |
| exposure | 0.2876 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
