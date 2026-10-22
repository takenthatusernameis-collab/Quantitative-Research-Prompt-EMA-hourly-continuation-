# EMA Hourly Continuation — APE/USDT P55_100

**Symbol:** APE/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 663 |
| net_profit_factor | 0.4965 |
| net_win_rate | 0.4796 |
| gross_profit_factor | 0.9092 |
| gross_win_rate | 0.4902 |
| sharpe_ratio | -4.8797 |
| sortino_ratio | -1.7689 |
| max_drawdown | 0.8846 |
| cagr | -0.5739 |
| net_avg_win | 27.3707 |
| net_avg_loss | -50.8114 |
| avg_hold_time_bars | 4.9306 |
| exposure | 0.1486 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
