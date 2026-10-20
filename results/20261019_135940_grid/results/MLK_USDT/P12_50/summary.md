# EMA Hourly Continuation — MLK/USDT P12_50

**Symbol:** MLK/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1352 |
| net_profit_factor | 0.3075 |
| net_win_rate | 0.2914 |
| gross_profit_factor | 0.6171 |
| gross_win_rate | 0.3062 |
| sharpe_ratio | -15.6509 |
| sortino_ratio | -8.2331 |
| max_drawdown | 1.0000 |
| cagr | -0.9850 |
| net_avg_win | 11.2683 |
| net_avg_loss | -15.0725 |
| avg_hold_time_bars | 5.9053 |
| exposure | 0.3613 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
