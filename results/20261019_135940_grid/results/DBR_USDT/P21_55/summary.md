# EMA Hourly Continuation — DBR/USDT P21_55

**Symbol:** DBR/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 617 |
| net_profit_factor | 0.5227 |
| net_win_rate | 0.4441 |
| gross_profit_factor | 0.9755 |
| gross_win_rate | 0.4749 |
| sharpe_ratio | -6.5124 |
| sortino_ratio | -2.5570 |
| max_drawdown | 0.9212 |
| cagr | -0.7089 |
| net_avg_win | 36.6144 |
| net_avg_loss | -55.9542 |
| avg_hold_time_bars | 7.8201 |
| exposure | 0.2744 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
