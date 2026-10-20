# EMA Hourly Continuation — ONT/USDT P100_200

**Symbol:** ONT/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 397 |
| net_profit_factor | 0.5267 |
| net_win_rate | 0.4408 |
| gross_profit_factor | 0.8408 |
| gross_win_rate | 0.4584 |
| sharpe_ratio | -3.8505 |
| sortino_ratio | -1.0814 |
| max_drawdown | 0.7323 |
| cagr | -0.4017 |
| net_avg_win | 46.1863 |
| net_avg_loss | -69.1262 |
| avg_hold_time_bars | 9.2821 |
| exposure | 0.1667 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
