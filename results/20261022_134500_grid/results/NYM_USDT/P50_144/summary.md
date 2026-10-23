# EMA Hourly Continuation — NYM/USDT P50_144

**Symbol:** NYM/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 472 |
| net_profit_factor | 0.2358 |
| net_win_rate | 0.3432 |
| gross_profit_factor | 0.5388 |
| gross_win_rate | 0.3856 |
| sharpe_ratio | -8.0851 |
| sortino_ratio | -2.5064 |
| max_drawdown | 0.9639 |
| cagr | -0.7299 |
| net_avg_win | 18.3347 |
| net_avg_loss | -40.6342 |
| avg_hold_time_bars | 11.7818 |
| exposure | 0.2528 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
