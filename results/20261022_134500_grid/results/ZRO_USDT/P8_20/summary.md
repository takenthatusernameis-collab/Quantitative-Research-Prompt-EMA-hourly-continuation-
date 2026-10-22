# EMA Hourly Continuation — ZRO/USDT P8_20

**Symbol:** ZRO/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1590 |
| net_profit_factor | 0.4268 |
| net_win_rate | 0.4365 |
| gross_profit_factor | 0.8182 |
| gross_win_rate | 0.4459 |
| sharpe_ratio | -11.0879 |
| sortino_ratio | -6.4562 |
| max_drawdown | 0.9995 |
| cagr | -0.9605 |
| net_avg_win | 10.7239 |
| net_avg_loss | -19.4610 |
| avg_hold_time_bars | 2.7830 |
| exposure | 0.2166 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
