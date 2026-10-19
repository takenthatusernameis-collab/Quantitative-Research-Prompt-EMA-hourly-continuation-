# EMA Hourly Continuation — ARB/USDT P26_100

**Symbol:** ARB/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 624 |
| net_profit_factor | 0.6881 |
| net_win_rate | 0.5080 |
| gross_profit_factor | 1.0640 |
| gross_win_rate | 0.5192 |
| sharpe_ratio | -2.8106 |
| sortino_ratio | -0.9936 |
| max_drawdown | 0.6973 |
| cagr | -0.3763 |
| net_avg_win | 48.3297 |
| net_avg_loss | -72.5230 |
| avg_hold_time_bars | 12.6394 |
| exposure | 0.3585 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
