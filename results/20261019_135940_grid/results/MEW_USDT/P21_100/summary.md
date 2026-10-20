# EMA Hourly Continuation — MEW/USDT P21_100

**Symbol:** MEW/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 657 |
| net_profit_factor | 0.5936 |
| net_win_rate | 0.4688 |
| gross_profit_factor | 0.8755 |
| gross_win_rate | 0.4749 |
| sharpe_ratio | -4.1230 |
| sortino_ratio | -1.4679 |
| max_drawdown | 0.8459 |
| cagr | -0.5144 |
| net_avg_win | 39.7029 |
| net_avg_loss | -59.0224 |
| avg_hold_time_bars | 13.7747 |
| exposure | 0.4114 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
