# EMA Hourly Continuation — TAO/USDT P50_200

**Symbol:** TAO/USDT  |  **P_fast:** 50  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 392 |
| net_profit_factor | 0.6799 |
| net_win_rate | 0.4847 |
| gross_profit_factor | 0.9394 |
| gross_win_rate | 0.4898 |
| sharpe_ratio | -2.3634 |
| sortino_ratio | -0.6603 |
| max_drawdown | 0.5542 |
| cagr | -0.2679 |
| net_avg_win | 60.6965 |
| net_avg_loss | -83.9694 |
| avg_hold_time_bars | 19.4592 |
| exposure | 0.3467 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
