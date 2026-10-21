# EMA Hourly Continuation — ZEC/USDT P8_200

**Symbol:** ZEC/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 248 |
| net_profit_factor | 0.9780 |
| net_win_rate | 0.5282 |
| gross_profit_factor | 1.0997 |
| gross_win_rate | 0.5282 |
| sharpe_ratio | -0.0563 |
| sortino_ratio | -0.0128 |
| max_drawdown | 0.1275 |
| cagr | -0.0105 |
| net_avg_win | 88.7067 |
| net_avg_loss | -101.5519 |
| avg_hold_time_bars | 72.1089 |
| exposure | 0.8129 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
