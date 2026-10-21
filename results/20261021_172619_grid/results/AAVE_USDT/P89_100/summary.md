# EMA Hourly Continuation — AAVE/USDT P89_100

**Symbol:** AAVE/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 91 |
| net_profit_factor | 0.6806 |
| net_win_rate | 0.4835 |
| gross_profit_factor | 0.9381 |
| gross_win_rate | 0.4835 |
| sharpe_ratio | -1.1491 |
| sortino_ratio | -0.1571 |
| max_drawdown | 0.1718 |
| cagr | -0.0694 |
| net_avg_win | 80.0490 |
| net_avg_loss | -110.1042 |
| avg_hold_time_bars | 5.0220 |
| exposure | 0.0208 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
