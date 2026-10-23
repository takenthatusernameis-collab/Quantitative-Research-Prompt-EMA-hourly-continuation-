# EMA Hourly Continuation — BRETT/USDT P26_200

**Symbol:** BRETT/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 280 |
| net_profit_factor | 0.7321 |
| net_win_rate | 0.4750 |
| gross_profit_factor | 0.8912 |
| gross_win_rate | 0.4750 |
| sharpe_ratio | -1.5896 |
| sortino_ratio | -0.3876 |
| max_drawdown | 0.3530 |
| cagr | -0.1661 |
| net_avg_win | 71.9296 |
| net_avg_loss | -88.8997 |
| avg_hold_time_bars | 47.8750 |
| exposure | 0.6450 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
