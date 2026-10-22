# EMA Hourly Continuation — AAVE/USDT P21_144

**Symbol:** AAVE/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 514 |
| net_profit_factor | 0.6407 |
| net_win_rate | 0.4922 |
| gross_profit_factor | 0.9474 |
| gross_win_rate | 0.4922 |
| sharpe_ratio | -3.0638 |
| sortino_ratio | -0.9668 |
| max_drawdown | 0.7213 |
| cagr | -0.3780 |
| net_avg_win | 49.0846 |
| net_avg_loss | -74.2683 |
| avg_hold_time_bars | 21.6401 |
| exposure | 0.5056 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
