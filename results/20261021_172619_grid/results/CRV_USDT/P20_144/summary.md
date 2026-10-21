# EMA Hourly Continuation — CRV/USDT P20_144

**Symbol:** CRV/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 398 |
| net_profit_factor | 0.8419 |
| net_win_rate | 0.4975 |
| gross_profit_factor | 1.0113 |
| gross_win_rate | 0.4975 |
| sharpe_ratio | -1.2464 |
| sortino_ratio | -0.3557 |
| max_drawdown | 0.4601 |
| cagr | -0.1523 |
| net_avg_win | 91.3315 |
| net_avg_loss | -107.4012 |
| avg_hold_time_bars | 26.1482 |
| exposure | 0.4730 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
