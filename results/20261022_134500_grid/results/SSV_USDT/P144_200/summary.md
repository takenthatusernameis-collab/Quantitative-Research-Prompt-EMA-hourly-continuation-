# EMA Hourly Continuation — SSV/USDT P144_200

**Symbol:** SSV/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 452 |
| net_profit_factor | 0.5501 |
| net_win_rate | 0.4735 |
| gross_profit_factor | 0.9634 |
| gross_win_rate | 0.4823 |
| sharpe_ratio | -4.1454 |
| sortino_ratio | -1.2403 |
| max_drawdown | 0.7832 |
| cagr | -0.4526 |
| net_avg_win | 44.6388 |
| net_avg_loss | -72.9654 |
| avg_hold_time_bars | 4.2566 |
| exposure | 0.0871 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
