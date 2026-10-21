# EMA Hourly Continuation — PUFFER/USDT P8_89

**Symbol:** PUFFER/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 411 |
| net_profit_factor | 0.9345 |
| net_win_rate | 0.5255 |
| gross_profit_factor | 1.0969 |
| gross_win_rate | 0.5255 |
| sharpe_ratio | -0.4122 |
| sortino_ratio | -0.1344 |
| max_drawdown | 0.2523 |
| cagr | -0.0668 |
| net_avg_win | 85.8992 |
| net_avg_loss | -101.8207 |
| avg_hold_time_bars | 27.0243 |
| exposure | 0.6285 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
