# EMA Hourly Continuation — DEEP/USDT P26_89

**Symbol:** DEEP/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 345 |
| net_profit_factor | 0.8827 |
| net_win_rate | 0.5130 |
| gross_profit_factor | 1.0513 |
| gross_win_rate | 0.5130 |
| sharpe_ratio | -0.8249 |
| sortino_ratio | -0.2453 |
| max_drawdown | 0.3023 |
| cagr | -0.1103 |
| net_avg_win | 89.2541 |
| net_avg_loss | -106.5306 |
| avg_hold_time_bars | 13.8029 |
| exposure | 0.2696 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
