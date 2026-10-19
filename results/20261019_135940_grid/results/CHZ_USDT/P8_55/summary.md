# EMA Hourly Continuation — CHZ/USDT P8_55

**Symbol:** CHZ/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1017 |
| net_profit_factor | 0.5528 |
| net_win_rate | 0.4710 |
| gross_profit_factor | 0.9175 |
| gross_win_rate | 0.4769 |
| sharpe_ratio | -6.0377 |
| sortino_ratio | -2.7039 |
| max_drawdown | 0.9650 |
| cagr | -0.7321 |
| net_avg_win | 24.8626 |
| net_avg_loss | -40.0430 |
| avg_hold_time_bars | 11.0816 |
| exposure | 0.5123 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
