# EMA Hourly Continuation — AIOZ/USDT P50_89

**Symbol:** AIOZ/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 362 |
| net_profit_factor | 0.8865 |
| net_win_rate | 0.5276 |
| gross_profit_factor | 1.1286 |
| gross_win_rate | 0.5276 |
| sharpe_ratio | -0.8005 |
| sortino_ratio | -0.2196 |
| max_drawdown | 0.3798 |
| cagr | -0.0988 |
| net_avg_win | 94.0252 |
| net_avg_loss | -118.4636 |
| avg_hold_time_bars | 7.6077 |
| exposure | 0.1252 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
