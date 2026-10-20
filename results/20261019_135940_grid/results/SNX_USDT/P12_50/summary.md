# EMA Hourly Continuation — SNX/USDT P12_50

**Symbol:** SNX/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1075 |
| net_profit_factor | 0.5925 |
| net_win_rate | 0.4698 |
| gross_profit_factor | 0.9965 |
| gross_win_rate | 0.4865 |
| sharpe_ratio | -5.8040 |
| sortino_ratio | -2.6779 |
| max_drawdown | 0.9605 |
| cagr | -0.7205 |
| net_avg_win | 27.6422 |
| net_avg_loss | -41.3300 |
| avg_hold_time_bars | 7.1098 |
| exposure | 0.3459 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
