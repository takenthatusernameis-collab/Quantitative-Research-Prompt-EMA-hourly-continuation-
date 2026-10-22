# EMA Hourly Continuation — INJ/USDT P21_89

**Symbol:** INJ/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 751 |
| net_profit_factor | 0.6355 |
| net_win_rate | 0.4754 |
| gross_profit_factor | 0.9429 |
| gross_win_rate | 0.4767 |
| sharpe_ratio | -4.3413 |
| sortino_ratio | -1.6751 |
| max_drawdown | 0.8678 |
| cagr | -0.5508 |
| net_avg_win | 42.3025 |
| net_avg_loss | -60.3100 |
| avg_hold_time_bars | 10.0839 |
| exposure | 0.3442 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
