# EMA Hourly Continuation — BOME/USDT P20_200

**Symbol:** BOME/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 273 |
| net_profit_factor | 0.8462 |
| net_win_rate | 0.4982 |
| gross_profit_factor | 0.9715 |
| gross_win_rate | 0.4982 |
| sharpe_ratio | -0.7923 |
| sortino_ratio | -0.1869 |
| max_drawdown | 0.2563 |
| cagr | -0.0843 |
| net_avg_win | 80.2290 |
| net_avg_loss | -94.1212 |
| avg_hold_time_bars | 52.3223 |
| exposure | 0.6493 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
