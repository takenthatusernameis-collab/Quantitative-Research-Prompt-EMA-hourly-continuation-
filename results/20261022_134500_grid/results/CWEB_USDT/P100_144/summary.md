# EMA Hourly Continuation — CWEB/USDT P100_144

**Symbol:** CWEB/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 389 |
| net_profit_factor | 0.3463 |
| net_win_rate | 0.3702 |
| gross_profit_factor | 0.7057 |
| gross_win_rate | 0.3805 |
| sharpe_ratio | -7.1946 |
| sortino_ratio | -2.0357 |
| max_drawdown | 0.9330 |
| cagr | -0.6559 |
| net_avg_win | 34.2707 |
| net_avg_loss | -58.1579 |
| avg_hold_time_bars | 7.0386 |
| exposure | 0.1245 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
