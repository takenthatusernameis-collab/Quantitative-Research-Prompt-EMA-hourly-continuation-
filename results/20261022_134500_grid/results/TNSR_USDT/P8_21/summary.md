# EMA Hourly Continuation — TNSR/USDT P8_21

**Symbol:** TNSR/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1605 |
| net_profit_factor | 0.5672 |
| net_win_rate | 0.4411 |
| gross_profit_factor | 1.0005 |
| gross_win_rate | 0.4579 |
| sharpe_ratio | -9.8683 |
| sortino_ratio | -5.5595 |
| max_drawdown | 0.9990 |
| cagr | -0.9345 |
| net_avg_win | 18.4926 |
| net_avg_loss | -25.7330 |
| avg_hold_time_bars | 3.2318 |
| exposure | 0.2347 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
