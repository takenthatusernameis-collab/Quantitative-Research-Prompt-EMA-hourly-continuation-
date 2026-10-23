# EMA Hourly Continuation — ORCA/USDT P20_26

**Symbol:** ORCA/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1078 |
| net_profit_factor | 0.3244 |
| net_win_rate | 0.3998 |
| gross_profit_factor | 0.7925 |
| gross_win_rate | 0.4443 |
| sharpe_ratio | -11.6003 |
| sortino_ratio | -5.4311 |
| max_drawdown | 0.9993 |
| cagr | -0.9431 |
| net_avg_win | 11.1347 |
| net_avg_loss | -22.8618 |
| avg_hold_time_bars | 2.7050 |
| exposure | 0.1325 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
