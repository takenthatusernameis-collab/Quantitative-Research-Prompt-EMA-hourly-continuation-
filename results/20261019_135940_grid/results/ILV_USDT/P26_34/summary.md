# EMA Hourly Continuation — ILV/USDT P26_34

**Symbol:** ILV/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1075 |
| net_profit_factor | 0.3050 |
| net_win_rate | 0.3870 |
| gross_profit_factor | 0.8324 |
| gross_win_rate | 0.4316 |
| sharpe_ratio | -12.3381 |
| sortino_ratio | -5.8441 |
| max_drawdown | 0.9995 |
| cagr | -0.9508 |
| net_avg_win | 10.5423 |
| net_avg_loss | -21.8215 |
| avg_hold_time_bars | 2.3023 |
| exposure | 0.1125 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
