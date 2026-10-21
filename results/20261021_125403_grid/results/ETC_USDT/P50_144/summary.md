# EMA Hourly Continuation — ETC/USDT P50_144

**Symbol:** ETC/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 356 |
| net_profit_factor | 0.7578 |
| net_win_rate | 0.5140 |
| gross_profit_factor | 1.0320 |
| gross_win_rate | 0.5140 |
| sharpe_ratio | -1.5285 |
| sortino_ratio | -0.4142 |
| max_drawdown | 0.4022 |
| cagr | -0.1732 |
| net_avg_win | 64.9257 |
| net_avg_loss | -90.6347 |
| avg_hold_time_bars | 14.8764 |
| exposure | 0.2407 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
