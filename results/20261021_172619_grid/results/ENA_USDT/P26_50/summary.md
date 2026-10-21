# EMA Hourly Continuation — ENA/USDT P26_50

**Symbol:** ENA/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 393 |
| net_profit_factor | 0.7634 |
| net_win_rate | 0.4860 |
| gross_profit_factor | 0.9442 |
| gross_win_rate | 0.4860 |
| sharpe_ratio | -1.6963 |
| sortino_ratio | -0.4804 |
| max_drawdown | 0.4621 |
| cagr | -0.1982 |
| net_avg_win | 71.9352 |
| net_avg_loss | -89.0938 |
| avg_hold_time_bars | 6.8779 |
| exposure | 0.1229 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
