# EMA Hourly Continuation — OP/USDT P100_200

**Symbol:** OP/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 252 |
| net_profit_factor | 1.0098 |
| net_win_rate | 0.5635 |
| gross_profit_factor | 1.2748 |
| gross_win_rate | 0.5635 |
| sharpe_ratio | 0.1032 |
| sortino_ratio | 0.0239 |
| max_drawdown | 0.1710 |
| cagr | 0.0053 |
| net_avg_win | 97.8265 |
| net_avg_loss | -125.0639 |
| avg_hold_time_bars | 12.8373 |
| exposure | 0.1470 |

Decision label: exploratory signal


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
