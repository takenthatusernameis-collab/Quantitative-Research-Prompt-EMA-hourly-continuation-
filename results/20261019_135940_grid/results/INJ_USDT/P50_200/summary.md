# EMA Hourly Continuation — INJ/USDT P50_200

**Symbol:** INJ/USDT  |  **P_fast:** 50  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 369 |
| net_profit_factor | 0.5468 |
| net_win_rate | 0.4444 |
| gross_profit_factor | 0.7786 |
| gross_win_rate | 0.4444 |
| sharpe_ratio | -3.3706 |
| sortino_ratio | -0.8970 |
| max_drawdown | 0.6818 |
| cagr | -0.3586 |
| net_avg_win | 49.4498 |
| net_avg_loss | -72.3471 |
| avg_hold_time_bars | 20.3577 |
| exposure | 0.3415 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
