# EMA Hourly Continuation — MLK/USDT P34_200

**Symbol:** MLK/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 581 |
| net_profit_factor | 0.3963 |
| net_win_rate | 0.3373 |
| gross_profit_factor | 0.5953 |
| gross_win_rate | 0.3408 |
| sharpe_ratio | -7.9111 |
| sortino_ratio | -2.6884 |
| max_drawdown | 0.9654 |
| cagr | -0.7332 |
| net_avg_win | 32.2920 |
| net_avg_loss | -41.4868 |
| avg_hold_time_bars | 17.0637 |
| exposure | 0.4487 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
