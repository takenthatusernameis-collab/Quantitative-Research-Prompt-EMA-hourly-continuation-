# EMA Hourly Continuation — BAND/USDT P12_200

**Symbol:** BAND/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 364 |
| net_profit_factor | 0.8339 |
| net_win_rate | 0.5275 |
| gross_profit_factor | 1.1412 |
| gross_win_rate | 0.5357 |
| sharpe_ratio | -1.0851 |
| sortino_ratio | -0.2918 |
| max_drawdown | 0.4142 |
| cagr | -0.1309 |
| net_avg_win | 77.9133 |
| net_avg_loss | -104.3014 |
| avg_hold_time_bars | 44.5604 |
| exposure | 0.7340 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
