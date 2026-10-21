# EMA Hourly Continuation — OP/USDT P8_200

**Symbol:** OP/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 229 |
| net_profit_factor | 0.8310 |
| net_win_rate | 0.4891 |
| gross_profit_factor | 0.9543 |
| gross_win_rate | 0.4891 |
| sharpe_ratio | -0.8897 |
| sortino_ratio | -0.1917 |
| max_drawdown | 0.2779 |
| cagr | -0.0859 |
| net_avg_win | 88.6850 |
| net_avg_loss | -102.1629 |
| avg_hold_time_bars | 79.6114 |
| exposure | 0.8287 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
