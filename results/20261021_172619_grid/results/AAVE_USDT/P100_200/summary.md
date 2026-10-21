# EMA Hourly Continuation — AAVE/USDT P100_200

**Symbol:** AAVE/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 247 |
| net_profit_factor | 0.7062 |
| net_win_rate | 0.4737 |
| gross_profit_factor | 0.8935 |
| gross_win_rate | 0.4737 |
| sharpe_ratio | -1.6763 |
| sortino_ratio | -0.3756 |
| max_drawdown | 0.3748 |
| cagr | -0.1582 |
| net_avg_win | 72.1219 |
| net_avg_loss | -91.9172 |
| avg_hold_time_bars | 13.3968 |
| exposure | 0.1504 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
