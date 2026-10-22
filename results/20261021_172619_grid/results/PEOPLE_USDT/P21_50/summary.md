# EMA Hourly Continuation — PEOPLE/USDT P21_50

**Symbol:** PEOPLE/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 546 |
| net_profit_factor | 0.6920 |
| net_win_rate | 0.4744 |
| gross_profit_factor | 0.8979 |
| gross_win_rate | 0.4744 |
| sharpe_ratio | -2.8030 |
| sortino_ratio | -0.9327 |
| max_drawdown | 0.6684 |
| cagr | -0.3475 |
| net_avg_win | 57.1829 |
| net_avg_loss | -74.5774 |
| avg_hold_time_bars | 6.8095 |
| exposure | 0.1682 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
