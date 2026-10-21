# EMA Hourly Continuation — SQD/USDT P8_21

**Symbol:** SQD/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 524 |
| net_profit_factor | 0.7710 |
| net_win_rate | 0.4905 |
| gross_profit_factor | 0.9750 |
| gross_win_rate | 0.4905 |
| sharpe_ratio | -2.0130 |
| sortino_ratio | -0.6700 |
| max_drawdown | 0.5758 |
| cagr | -0.2652 |
| net_avg_win | 69.0254 |
| net_avg_loss | -86.1705 |
| avg_hold_time_bars | 5.3798 |
| exposure | 0.1325 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
