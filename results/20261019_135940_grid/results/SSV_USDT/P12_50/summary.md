# EMA Hourly Continuation — SSV/USDT P12_50

**Symbol:** SSV/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1137 |
| net_profit_factor | 0.6006 |
| net_win_rate | 0.4459 |
| gross_profit_factor | 0.9136 |
| gross_win_rate | 0.4556 |
| sharpe_ratio | -6.7559 |
| sortino_ratio | -3.2098 |
| max_drawdown | 0.9800 |
| cagr | -0.7832 |
| net_avg_win | 29.0275 |
| net_avg_loss | -38.8976 |
| avg_hold_time_bars | 7.1152 |
| exposure | 0.3661 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
