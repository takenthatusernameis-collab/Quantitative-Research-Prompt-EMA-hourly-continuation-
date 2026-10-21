# EMA Hourly Continuation — VET/USDT P26_100

**Symbol:** VET/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 473 |
| net_profit_factor | 0.8166 |
| net_win_rate | 0.5137 |
| gross_profit_factor | 1.0558 |
| gross_win_rate | 0.5137 |
| sharpe_ratio | -1.4212 |
| sortino_ratio | -0.4440 |
| max_drawdown | 0.4515 |
| cagr | -0.1858 |
| net_avg_win | 73.8472 |
| net_avg_loss | -95.5492 |
| avg_hold_time_bars | 14.6152 |
| exposure | 0.3142 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
