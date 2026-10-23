# EMA Hourly Continuation — AVA/USDT P12_200

**Symbol:** AVA/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 466 |
| net_profit_factor | 0.6017 |
| net_win_rate | 0.4764 |
| gross_profit_factor | 0.8969 |
| gross_win_rate | 0.4850 |
| sharpe_ratio | -2.9231 |
| sortino_ratio | -0.8781 |
| max_drawdown | 0.6815 |
| cagr | -0.3495 |
| net_avg_win | 44.9441 |
| net_avg_loss | -67.9582 |
| avg_hold_time_bars | 31.6996 |
| exposure | 0.6715 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
