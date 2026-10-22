# EMA Hourly Continuation — STX/USDT P34_200

**Symbol:** STX/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 360 |
| net_profit_factor | 0.7989 |
| net_win_rate | 0.5222 |
| gross_profit_factor | 1.1082 |
| gross_win_rate | 0.5306 |
| sharpe_ratio | -1.2465 |
| sortino_ratio | -0.3367 |
| max_drawdown | 0.3727 |
| cagr | -0.1460 |
| net_avg_win | 69.3893 |
| net_avg_loss | -94.9374 |
| avg_hold_time_bars | 32.0222 |
| exposure | 0.5217 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
