# EMA Hourly Continuation — W/USDT P26_89

**Symbol:** W/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 484 |
| net_profit_factor | 0.8515 |
| net_win_rate | 0.5124 |
| gross_profit_factor | 1.0450 |
| gross_win_rate | 0.5124 |
| sharpe_ratio | -1.0799 |
| sortino_ratio | -0.3412 |
| max_drawdown | 0.4033 |
| cagr | -0.1476 |
| net_avg_win | 76.3725 |
| net_avg_loss | -94.2569 |
| avg_hold_time_bars | 13.0062 |
| exposure | 0.2861 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
