# EMA Hourly Continuation — DEEP/USDT P8_34

**Symbol:** DEEP/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 598 |
| net_profit_factor | 0.9476 |
| net_win_rate | 0.5385 |
| gross_profit_factor | 1.1605 |
| gross_win_rate | 0.5385 |
| sharpe_ratio | -0.4360 |
| sortino_ratio | -0.1720 |
| max_drawdown | 0.3153 |
| cagr | -0.0862 |
| net_avg_win | 93.2836 |
| net_avg_loss | -114.8485 |
| avg_hold_time_bars | 8.0702 |
| exposure | 0.2732 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
