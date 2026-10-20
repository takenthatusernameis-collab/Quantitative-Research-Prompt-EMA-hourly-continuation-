# EMA Hourly Continuation — TRB/USDT P55_100

**Symbol:** TRB/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 667 |
| net_profit_factor | 0.4325 |
| net_win_rate | 0.4303 |
| gross_profit_factor | 0.7733 |
| gross_win_rate | 0.4498 |
| sharpe_ratio | -6.5143 |
| sortino_ratio | -2.3751 |
| max_drawdown | 0.9461 |
| cagr | -0.6851 |
| net_avg_win | 25.1196 |
| net_avg_loss | -43.8607 |
| avg_hold_time_bars | 5.6357 |
| exposure | 0.1701 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
