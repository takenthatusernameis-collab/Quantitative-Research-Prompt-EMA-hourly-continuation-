# EMA Hourly Continuation — SNX/USDT P8_200

**Symbol:** SNX/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 363 |
| net_profit_factor | 0.8887 |
| net_win_rate | 0.5372 |
| gross_profit_factor | 1.1664 |
| gross_win_rate | 0.5399 |
| sharpe_ratio | -0.6564 |
| sortino_ratio | -0.1784 |
| max_drawdown | 0.2262 |
| cagr | -0.0832 |
| net_avg_win | 80.5825 |
| net_avg_loss | -105.2471 |
| avg_hold_time_bars | 48.2948 |
| exposure | 0.7933 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
