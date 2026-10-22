# EMA Hourly Continuation — GRAM/USDT P12_144

**Symbol:** GRAM/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 532 |
| net_profit_factor | 0.4951 |
| net_win_rate | 0.4586 |
| gross_profit_factor | 0.9301 |
| gross_win_rate | 0.4774 |
| sharpe_ratio | -4.6813 |
| sortino_ratio | -1.5055 |
| max_drawdown | 0.8581 |
| cagr | -0.5270 |
| net_avg_win | 34.0553 |
| net_avg_loss | -58.2765 |
| avg_hold_time_bars | 27.1278 |
| exposure | 0.6560 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
