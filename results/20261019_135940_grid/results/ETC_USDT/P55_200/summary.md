# EMA Hourly Continuation — ETC/USDT P55_200

**Symbol:** ETC/USDT  |  **P_fast:** 55  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 409 |
| net_profit_factor | 0.6264 |
| net_win_rate | 0.4890 |
| gross_profit_factor | 0.9970 |
| gross_win_rate | 0.5037 |
| sharpe_ratio | -3.0326 |
| sortino_ratio | -0.8643 |
| max_drawdown | 0.6483 |
| cagr | -0.3377 |
| net_avg_win | 54.0321 |
| net_avg_loss | -82.5501 |
| avg_hold_time_bars | 19.1907 |
| exposure | 0.3568 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
