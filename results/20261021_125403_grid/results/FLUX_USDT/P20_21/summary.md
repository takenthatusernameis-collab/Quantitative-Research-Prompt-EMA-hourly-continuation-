# EMA Hourly Continuation — FLUX/USDT P20_21

**Symbol:** FLUX/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 130 |
| net_profit_factor | 0.5939 |
| net_win_rate | 0.4462 |
| gross_profit_factor | 0.8098 |
| gross_win_rate | 0.4462 |
| sharpe_ratio | -1.8648 |
| sortino_ratio | -0.3032 |
| max_drawdown | 0.3117 |
| cagr | -0.1299 |
| net_avg_win | 74.3849 |
| net_avg_loss | -100.8865 |
| avg_hold_time_bars | 4.1692 |
| exposure | 0.0246 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
