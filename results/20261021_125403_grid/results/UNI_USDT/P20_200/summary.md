# EMA Hourly Continuation — UNI/USDT P20_200

**Symbol:** UNI/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 273 |
| net_profit_factor | 0.8928 |
| net_win_rate | 0.5128 |
| gross_profit_factor | 1.0363 |
| gross_win_rate | 0.5128 |
| sharpe_ratio | -0.5429 |
| sortino_ratio | -0.1285 |
| max_drawdown | 0.1763 |
| cagr | -0.0601 |
| net_avg_win | 85.7670 |
| net_avg_loss | -101.1260 |
| avg_hold_time_bars | 50.0733 |
| exposure | 0.6214 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
