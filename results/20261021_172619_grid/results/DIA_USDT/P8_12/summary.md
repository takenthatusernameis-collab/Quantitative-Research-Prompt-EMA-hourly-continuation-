# EMA Hourly Continuation — DIA/USDT P8_12

**Symbol:** DIA/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 458 |
| net_profit_factor | 0.5780 |
| net_win_rate | 0.4847 |
| gross_profit_factor | 0.8833 |
| gross_win_rate | 0.4869 |
| sharpe_ratio | -3.2323 |
| sortino_ratio | -0.9908 |
| max_drawdown | 0.6822 |
| cagr | -0.3652 |
| net_avg_win | 42.0860 |
| net_avg_loss | -68.4947 |
| avg_hold_time_bars | 4.5459 |
| exposure | 0.0942 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
