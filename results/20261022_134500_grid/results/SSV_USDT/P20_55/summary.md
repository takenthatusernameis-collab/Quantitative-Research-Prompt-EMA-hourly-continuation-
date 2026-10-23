# EMA Hourly Continuation — SSV/USDT P20_55

**Symbol:** SSV/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1023 |
| net_profit_factor | 0.5542 |
| net_win_rate | 0.4467 |
| gross_profit_factor | 0.8799 |
| gross_win_rate | 0.4594 |
| sharpe_ratio | -6.7290 |
| sortino_ratio | -3.0185 |
| max_drawdown | 0.9767 |
| cagr | -0.7674 |
| net_avg_win | 26.5112 |
| net_avg_loss | -38.6275 |
| avg_hold_time_bars | 5.7038 |
| exposure | 0.2640 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
