# EMA Hourly Continuation — MINA/USDT P50_55

**Symbol:** MINA/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 167 |
| net_profit_factor | 0.6424 |
| net_win_rate | 0.5090 |
| gross_profit_factor | 1.0371 |
| gross_win_rate | 0.5090 |
| sharpe_ratio | -1.8094 |
| sortino_ratio | -0.3352 |
| max_drawdown | 0.3751 |
| cagr | -0.1442 |
| net_avg_win | 68.4193 |
| net_avg_loss | -110.3996 |
| avg_hold_time_bars | 4.7305 |
| exposure | 0.0359 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
