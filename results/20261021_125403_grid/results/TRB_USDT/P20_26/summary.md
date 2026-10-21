# EMA Hourly Continuation — TRB/USDT P20_26

**Symbol:** TRB/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 224 |
| net_profit_factor | 0.4381 |
| net_win_rate | 0.3750 |
| gross_profit_factor | 0.6369 |
| gross_win_rate | 0.3750 |
| sharpe_ratio | -4.0820 |
| sortino_ratio | -0.8702 |
| max_drawdown | 0.6454 |
| cagr | -0.3333 |
| net_avg_win | 59.4235 |
| net_avg_loss | -81.3916 |
| avg_hold_time_bars | 4.6384 |
| exposure | 0.0470 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
