# EMA Hourly Continuation — VR/USDT P12_55

**Symbol:** VR/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1068 |
| net_profit_factor | 0.4677 |
| net_win_rate | 0.3605 |
| gross_profit_factor | 0.7201 |
| gross_win_rate | 0.3745 |
| sharpe_ratio | -11.8126 |
| sortino_ratio | -5.3438 |
| max_drawdown | 0.9995 |
| cagr | -0.9516 |
| net_avg_win | 22.8092 |
| net_avg_loss | -27.4913 |
| avg_hold_time_bars | 7.9822 |
| exposure | 0.3875 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
