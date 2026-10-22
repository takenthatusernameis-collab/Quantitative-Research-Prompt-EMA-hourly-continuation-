# EMA Hourly Continuation — SSV/USDT P26_200

**Symbol:** SSV/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 286 |
| net_profit_factor | 0.8594 |
| net_win_rate | 0.5070 |
| gross_profit_factor | 1.0255 |
| gross_win_rate | 0.5105 |
| sharpe_ratio | -0.7600 |
| sortino_ratio | -0.1837 |
| max_drawdown | 0.2325 |
| cagr | -0.0831 |
| net_avg_win | 82.8582 |
| net_avg_loss | -99.1527 |
| avg_hold_time_bars | 46.1713 |
| exposure | 0.5975 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
