# EMA Hourly Continuation — FET/USDT P34_200

**Symbol:** FET/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 365 |
| net_profit_factor | 0.7467 |
| net_win_rate | 0.5068 |
| gross_profit_factor | 0.9906 |
| gross_win_rate | 0.5068 |
| sharpe_ratio | -1.5597 |
| sortino_ratio | -0.4217 |
| max_drawdown | 0.4077 |
| cagr | -0.1814 |
| net_avg_win | 62.9539 |
| net_avg_loss | -86.6477 |
| avg_hold_time_bars | 29.1562 |
| exposure | 0.4837 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
