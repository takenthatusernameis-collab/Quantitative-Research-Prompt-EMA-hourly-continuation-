# EMA Hourly Continuation — YGG/USDT P21_55

**Symbol:** YGG/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 548 |
| net_profit_factor | 0.7640 |
| net_win_rate | 0.4945 |
| gross_profit_factor | 0.9898 |
| gross_win_rate | 0.4945 |
| sharpe_ratio | -2.1409 |
| sortino_ratio | -0.7159 |
| max_drawdown | 0.5698 |
| cagr | -0.2801 |
| net_avg_win | 67.3075 |
| net_avg_loss | -86.1922 |
| avg_hold_time_bars | 8.1350 |
| exposure | 0.2017 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
