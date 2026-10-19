# EMA Hourly Continuation — SEI/USDT P55_100

**Symbol:** SEI/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 593 |
| net_profit_factor | 0.5681 |
| net_win_rate | 0.4553 |
| gross_profit_factor | 0.8913 |
| gross_win_rate | 0.4621 |
| sharpe_ratio | -4.9126 |
| sortino_ratio | -1.6949 |
| max_drawdown | 0.8712 |
| cagr | -0.5564 |
| net_avg_win | 42.3847 |
| net_avg_loss | -62.3689 |
| avg_hold_time_bars | 5.4115 |
| exposure | 0.1459 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
