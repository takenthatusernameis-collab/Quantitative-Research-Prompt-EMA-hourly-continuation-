# EMA Hourly Continuation — AR/USDT P21_26

**Symbol:** AR/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1191 |
| net_profit_factor | 0.2596 |
| net_win_rate | 0.3644 |
| gross_profit_factor | 0.6569 |
| gross_win_rate | 0.4005 |
| sharpe_ratio | -13.8418 |
| sortino_ratio | -6.8631 |
| max_drawdown | 0.9999 |
| cagr | -0.9742 |
| net_avg_win | 8.0777 |
| net_avg_loss | -17.8398 |
| avg_hold_time_bars | 1.9001 |
| exposure | 0.1029 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
