# EMA Hourly Continuation — EGLD/USDT P100_200

**Symbol:** EGLD/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 371 |
| net_profit_factor | 0.5417 |
| net_win_rate | 0.4744 |
| gross_profit_factor | 0.8756 |
| gross_win_rate | 0.4906 |
| sharpe_ratio | -2.9841 |
| sortino_ratio | -0.8187 |
| max_drawdown | 0.6222 |
| cagr | -0.3156 |
| net_avg_win | 41.2554 |
| net_avg_loss | -68.7325 |
| avg_hold_time_bars | 10.0701 |
| exposure | 0.1698 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
