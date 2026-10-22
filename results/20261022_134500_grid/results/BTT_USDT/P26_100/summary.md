# EMA Hourly Continuation — BTT/USDT P26_100

**Symbol:** BTT/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 608 |
| net_profit_factor | 0.3830 |
| net_win_rate | 0.3651 |
| gross_profit_factor | 0.7865 |
| gross_win_rate | 0.4013 |
| sharpe_ratio | -9.4356 |
| sortino_ratio | -3.3339 |
| max_drawdown | 0.9884 |
| cagr | -0.8304 |
| net_avg_win | 27.6409 |
| net_avg_loss | -41.5031 |
| avg_hold_time_bars | 14.7188 |
| exposure | 0.4068 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
