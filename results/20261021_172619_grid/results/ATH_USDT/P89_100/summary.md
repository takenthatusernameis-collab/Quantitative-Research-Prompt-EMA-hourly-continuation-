# EMA Hourly Continuation — ATH/USDT P89_100

**Symbol:** ATH/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 97 |
| net_profit_factor | 0.6642 |
| net_win_rate | 0.4742 |
| gross_profit_factor | 0.9032 |
| gross_win_rate | 0.4742 |
| sharpe_ratio | -1.3063 |
| sortino_ratio | -0.1900 |
| max_drawdown | 0.2152 |
| cagr | -0.0839 |
| net_avg_win | 80.2052 |
| net_avg_loss | -108.9162 |
| avg_hold_time_bars | 5.2990 |
| exposure | 0.0249 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
