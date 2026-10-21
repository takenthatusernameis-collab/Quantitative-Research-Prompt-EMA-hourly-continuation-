# EMA Hourly Continuation — PUNDIX/USDT P8_200

**Symbol:** PUNDIX/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 326 |
| net_profit_factor | 0.8260 |
| net_win_rate | 0.5123 |
| gross_profit_factor | 1.0328 |
| gross_win_rate | 0.5153 |
| sharpe_ratio | -0.9704 |
| sortino_ratio | -0.2510 |
| max_drawdown | 0.3384 |
| cagr | -0.1113 |
| net_avg_win | 72.8877 |
| net_avg_loss | -92.6859 |
| avg_hold_time_bars | 52.8344 |
| exposure | 0.7829 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
