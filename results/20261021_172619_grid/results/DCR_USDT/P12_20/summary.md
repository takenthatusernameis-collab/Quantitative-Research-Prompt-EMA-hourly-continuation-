# EMA Hourly Continuation — DCR/USDT P12_20

**Symbol:** DCR/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 478 |
| net_profit_factor | 0.6157 |
| net_win_rate | 0.4937 |
| gross_profit_factor | 0.9918 |
| gross_win_rate | 0.4937 |
| sharpe_ratio | -3.3075 |
| sortino_ratio | -1.0373 |
| max_drawdown | 0.7045 |
| cagr | -0.3797 |
| net_avg_win | 47.5386 |
| net_avg_loss | -75.2933 |
| avg_hold_time_bars | 5.1088 |
| exposure | 0.1105 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
