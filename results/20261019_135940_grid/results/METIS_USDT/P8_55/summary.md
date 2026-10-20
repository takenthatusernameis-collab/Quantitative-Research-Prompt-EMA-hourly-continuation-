# EMA Hourly Continuation — METIS/USDT P8_55

**Symbol:** METIS/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1000 |
| net_profit_factor | 0.5946 |
| net_win_rate | 0.4560 |
| gross_profit_factor | 0.9061 |
| gross_win_rate | 0.4670 |
| sharpe_ratio | -5.7295 |
| sortino_ratio | -2.5482 |
| max_drawdown | 0.9554 |
| cagr | -0.7049 |
| net_avg_win | 30.6619 |
| net_avg_loss | -43.2262 |
| avg_hold_time_bars | 11.3160 |
| exposure | 0.5144 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
