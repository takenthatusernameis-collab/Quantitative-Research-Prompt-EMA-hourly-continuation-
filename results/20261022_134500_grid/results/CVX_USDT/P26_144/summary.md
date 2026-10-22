# EMA Hourly Continuation — CVX/USDT P26_144

**Symbol:** CVX/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 507 |
| net_profit_factor | 0.6401 |
| net_win_rate | 0.4694 |
| gross_profit_factor | 0.8867 |
| gross_win_rate | 0.4753 |
| sharpe_ratio | -3.0484 |
| sortino_ratio | -0.9680 |
| max_drawdown | 0.6869 |
| cagr | -0.3678 |
| net_avg_win | 51.1013 |
| net_avg_loss | -70.6356 |
| avg_hold_time_bars | 19.2564 |
| exposure | 0.4438 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
