# EMA Hourly Continuation — POKT/USDT P89_100

**Symbol:** POKT/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 698 |
| net_profit_factor | 0.2832 |
| net_win_rate | 0.3438 |
| gross_profit_factor | 0.7120 |
| gross_win_rate | 0.3825 |
| sharpe_ratio | -10.4275 |
| sortino_ratio | -3.9494 |
| max_drawdown | 0.9944 |
| cagr | -0.8715 |
| net_avg_win | 16.3683 |
| net_avg_loss | -30.2880 |
| avg_hold_time_bars | 3.1261 |
| exposure | 0.0987 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
