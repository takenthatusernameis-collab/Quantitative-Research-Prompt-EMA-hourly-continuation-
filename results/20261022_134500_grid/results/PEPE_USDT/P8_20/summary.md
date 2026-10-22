# EMA Hourly Continuation — PEPE/USDT P8_20

**Symbol:** PEPE/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1725 |
| net_profit_factor | 0.4639 |
| net_win_rate | 0.4348 |
| gross_profit_factor | 0.8381 |
| gross_win_rate | 0.4528 |
| sharpe_ratio | -11.8431 |
| sortino_ratio | -6.9167 |
| max_drawdown | 0.9999 |
| cagr | -0.9705 |
| net_avg_win | 11.5381 |
| net_avg_loss | -19.1304 |
| avg_hold_time_bars | 2.4777 |
| exposure | 0.1943 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
