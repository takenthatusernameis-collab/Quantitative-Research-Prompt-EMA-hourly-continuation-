# EMA Hourly Continuation — BTT/USDT P20_100

**Symbol:** BTT/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 599 |
| net_profit_factor | 0.3868 |
| net_win_rate | 0.3740 |
| gross_profit_factor | 0.7871 |
| gross_win_rate | 0.4124 |
| sharpe_ratio | -9.0086 |
| sortino_ratio | -3.1506 |
| max_drawdown | 0.9848 |
| cagr | -0.8106 |
| net_avg_win | 27.7305 |
| net_avg_loss | -42.8227 |
| avg_hold_time_bars | 17.9482 |
| exposure | 0.4887 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
