# EMA Hourly Continuation — SSV/USDT P8_200

**Symbol:** SSV/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 250 |
| net_profit_factor | 0.7285 |
| net_win_rate | 0.4920 |
| gross_profit_factor | 0.9780 |
| gross_win_rate | 0.5000 |
| sharpe_ratio | -1.4505 |
| sortino_ratio | -0.3233 |
| max_drawdown | 0.3594 |
| cagr | -0.1413 |
| net_avg_win | 69.6183 |
| net_avg_loss | -92.5493 |
| avg_hold_time_bars | 76.9320 |
| exposure | 0.8703 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
