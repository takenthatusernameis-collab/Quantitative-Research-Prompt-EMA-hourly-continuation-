# EMA Hourly Continuation — ASTR/USDT P8_200

**Symbol:** ASTR/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 260 |
| net_profit_factor | 0.9286 |
| net_win_rate | 0.5346 |
| gross_profit_factor | 1.1326 |
| gross_win_rate | 0.5346 |
| sharpe_ratio | -0.3454 |
| sortino_ratio | -0.0800 |
| max_drawdown | 0.2080 |
| cagr | -0.0394 |
| net_avg_win | 90.2800 |
| net_avg_loss | -111.6817 |
| avg_hold_time_bars | 70.9077 |
| exposure | 0.8343 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
