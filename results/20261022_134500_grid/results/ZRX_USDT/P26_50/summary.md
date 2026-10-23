# EMA Hourly Continuation — ZRX/USDT P26_50

**Symbol:** ZRX/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 936 |
| net_profit_factor | 0.4021 |
| net_win_rate | 0.4284 |
| gross_profit_factor | 0.7969 |
| gross_win_rate | 0.4487 |
| sharpe_ratio | -8.3015 |
| sortino_ratio | -3.5800 |
| max_drawdown | 0.9886 |
| cagr | -0.8307 |
| net_avg_win | 16.5750 |
| net_avg_loss | -30.8992 |
| avg_hold_time_bars | 4.6357 |
| exposure | 0.1972 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
