# EMA Hourly Continuation — KCS/USDT P100_144

**Symbol:** KCS/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 509 |
| net_profit_factor | 0.1754 |
| net_win_rate | 0.3536 |
| gross_profit_factor | 0.6850 |
| gross_win_rate | 0.4322 |
| sharpe_ratio | -9.7897 |
| sortino_ratio | -3.2727 |
| max_drawdown | 0.9884 |
| cagr | -0.8290 |
| net_avg_win | 11.6757 |
| net_avg_loss | -36.4230 |
| avg_hold_time_bars | 5.0491 |
| exposure | 0.1168 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
