# EMA Hourly Continuation — GRAM/USDT P20_26

**Symbol:** GRAM/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1222 |
| net_profit_factor | 0.1466 |
| net_win_rate | 0.3298 |
| gross_profit_factor | 0.5422 |
| gross_win_rate | 0.3912 |
| sharpe_ratio | -16.9269 |
| sortino_ratio | -8.8963 |
| max_drawdown | 1.0000 |
| cagr | -0.9928 |
| net_avg_win | 4.2622 |
| net_avg_loss | -14.3072 |
| avg_hold_time_bars | 1.8159 |
| exposure | 0.1009 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
