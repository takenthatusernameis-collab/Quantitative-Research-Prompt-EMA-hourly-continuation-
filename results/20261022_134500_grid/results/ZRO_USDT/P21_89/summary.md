# EMA Hourly Continuation — ZRO/USDT P21_89

**Symbol:** ZRO/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 671 |
| net_profit_factor | 0.6755 |
| net_win_rate | 0.4799 |
| gross_profit_factor | 0.9447 |
| gross_win_rate | 0.4829 |
| sharpe_ratio | -3.4025 |
| sortino_ratio | -1.2870 |
| max_drawdown | 0.7676 |
| cagr | -0.4588 |
| net_avg_win | 49.2129 |
| net_avg_loss | -67.2153 |
| avg_hold_time_bars | 11.1252 |
| exposure | 0.3654 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
