# EMA Hourly Continuation — STX/USDT P8_12

**Symbol:** STX/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 244 |
| net_profit_factor | 0.7980 |
| net_win_rate | 0.5369 |
| gross_profit_factor | 1.1341 |
| gross_win_rate | 0.5369 |
| sharpe_ratio | -0.9904 |
| sortino_ratio | -0.2235 |
| max_drawdown | 0.2345 |
| cagr | -0.0973 |
| net_avg_win | 68.5858 |
| net_avg_loss | -99.6432 |
| avg_hold_time_bars | 5.0656 |
| exposure | 0.0559 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
