# EMA Hourly Continuation — CGPT/USDT P55_200

**Symbol:** CGPT/USDT  |  **P_fast:** 55  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 381 |
| net_profit_factor | 0.6397 |
| net_win_rate | 0.4646 |
| gross_profit_factor | 0.9014 |
| gross_win_rate | 0.4672 |
| sharpe_ratio | -2.9754 |
| sortino_ratio | -0.8156 |
| max_drawdown | 0.6326 |
| cagr | -0.3238 |
| net_avg_win | 62.7472 |
| net_avg_loss | -85.1090 |
| avg_hold_time_bars | 20.8346 |
| exposure | 0.3608 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
