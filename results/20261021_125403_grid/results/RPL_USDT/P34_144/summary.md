# EMA Hourly Continuation — RPL/USDT P34_144

**Symbol:** RPL/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 381 |
| net_profit_factor | 0.8239 |
| net_win_rate | 0.4987 |
| gross_profit_factor | 0.9993 |
| gross_win_rate | 0.4987 |
| sharpe_ratio | -1.1976 |
| sortino_ratio | -0.3337 |
| max_drawdown | 0.3950 |
| cagr | -0.1435 |
| net_avg_win | 79.6418 |
| net_avg_loss | -96.1623 |
| avg_hold_time_bars | 24.6273 |
| exposure | 0.4246 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
