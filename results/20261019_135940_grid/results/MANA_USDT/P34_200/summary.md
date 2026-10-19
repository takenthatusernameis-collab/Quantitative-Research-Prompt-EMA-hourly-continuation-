# EMA Hourly Continuation — MANA/USDT P34_200

**Symbol:** MANA/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 375 |
| net_profit_factor | 0.6480 |
| net_win_rate | 0.4880 |
| gross_profit_factor | 0.9777 |
| gross_win_rate | 0.4933 |
| sharpe_ratio | -2.7069 |
| sortino_ratio | -0.7302 |
| max_drawdown | 0.6092 |
| cagr | -0.3024 |
| net_avg_win | 59.8786 |
| net_avg_loss | -88.0684 |
| avg_hold_time_bars | 32.7013 |
| exposure | 0.5574 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
