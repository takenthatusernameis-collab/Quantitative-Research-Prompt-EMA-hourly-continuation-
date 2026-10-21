# EMA Hourly Continuation — ELON/USDT P12_55

**Symbol:** ELON/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 589 |
| net_profit_factor | 0.7242 |
| net_win_rate | 0.4788 |
| gross_profit_factor | 0.9299 |
| gross_win_rate | 0.4788 |
| sharpe_ratio | -2.6441 |
| sortino_ratio | -0.9160 |
| max_drawdown | 0.6558 |
| cagr | -0.3431 |
| net_avg_win | 60.7106 |
| net_avg_loss | -77.0010 |
| avg_hold_time_bars | 11.6859 |
| exposure | 0.3129 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
