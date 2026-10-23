# EMA Hourly Continuation — RIO/USDT P55_89

**Symbol:** RIO/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 780 |
| net_profit_factor | 0.4235 |
| net_win_rate | 0.3756 |
| gross_profit_factor | 0.6253 |
| gross_win_rate | 0.3808 |
| sharpe_ratio | -8.1297 |
| sortino_ratio | -3.1993 |
| max_drawdown | 0.9813 |
| cagr | -0.7951 |
| net_avg_win | 24.5848 |
| net_avg_loss | -34.9266 |
| avg_hold_time_bars | 3.4564 |
| exposure | 0.1238 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
