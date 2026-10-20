# EMA Hourly Continuation — 1INCH/USDT P8_34

**Symbol:** 1INCH/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1410 |
| net_profit_factor | 0.4544 |
| net_win_rate | 0.4447 |
| gross_profit_factor | 0.8500 |
| gross_win_rate | 0.4702 |
| sharpe_ratio | -9.5246 |
| sortino_ratio | -5.0358 |
| max_drawdown | 0.9981 |
| cagr | -0.9182 |
| net_avg_win | 13.2570 |
| net_avg_loss | -23.3634 |
| avg_hold_time_bars | 5.2979 |
| exposure | 0.3395 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
