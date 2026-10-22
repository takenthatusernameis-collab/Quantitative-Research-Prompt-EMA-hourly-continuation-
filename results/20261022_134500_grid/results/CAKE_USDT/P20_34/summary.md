# EMA Hourly Continuation — CAKE/USDT P20_34

**Symbol:** CAKE/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1089 |
| net_profit_factor | 0.2950 |
| net_win_rate | 0.4022 |
| gross_profit_factor | 0.8680 |
| gross_win_rate | 0.4444 |
| sharpe_ratio | -11.7109 |
| sortino_ratio | -5.5400 |
| max_drawdown | 0.9992 |
| cagr | -0.9424 |
| net_avg_win | 9.5470 |
| net_avg_loss | -21.7724 |
| avg_hold_time_bars | 2.9908 |
| exposure | 0.1480 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
