# EMA Hourly Continuation — EUL/USDT P144_200

**Symbol:** EUL/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 381 |
| net_profit_factor | 0.3954 |
| net_win_rate | 0.4068 |
| gross_profit_factor | 0.7225 |
| gross_win_rate | 0.4304 |
| sharpe_ratio | -5.1696 |
| sortino_ratio | -1.4323 |
| max_drawdown | 0.8283 |
| cagr | -0.4992 |
| net_avg_win | 34.7695 |
| net_avg_loss | -60.3033 |
| avg_hold_time_bars | 4.5013 |
| exposure | 0.0780 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
