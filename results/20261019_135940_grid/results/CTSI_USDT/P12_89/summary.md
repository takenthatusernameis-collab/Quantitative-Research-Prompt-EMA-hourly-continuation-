# EMA Hourly Continuation — CTSI/USDT P12_89

**Symbol:** CTSI/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 751 |
| net_profit_factor | 0.6381 |
| net_win_rate | 0.4687 |
| gross_profit_factor | 0.9778 |
| gross_win_rate | 0.4767 |
| sharpe_ratio | -4.4200 |
| sortino_ratio | -1.7099 |
| max_drawdown | 0.8707 |
| cagr | -0.5544 |
| net_avg_win | 43.5084 |
| net_avg_loss | -60.1534 |
| avg_hold_time_bars | 15.4075 |
| exposure | 0.5260 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
