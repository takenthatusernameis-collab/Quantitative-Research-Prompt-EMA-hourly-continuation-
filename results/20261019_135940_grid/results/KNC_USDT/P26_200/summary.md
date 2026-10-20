# EMA Hourly Continuation — KNC/USDT P26_200

**Symbol:** KNC/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 359 |
| net_profit_factor | 0.7780 |
| net_win_rate | 0.5265 |
| gross_profit_factor | 1.1267 |
| gross_win_rate | 0.5292 |
| sharpe_ratio | -1.5471 |
| sortino_ratio | -0.4154 |
| max_drawdown | 0.4667 |
| cagr | -0.1795 |
| net_avg_win | 72.6047 |
| net_avg_loss | -103.7490 |
| avg_hold_time_bars | 37.5515 |
| exposure | 0.6128 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
