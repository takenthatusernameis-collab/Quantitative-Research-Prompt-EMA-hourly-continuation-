# EMA Hourly Continuation — AR/USDT P12_26

**Symbol:** AR/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 462 |
| net_profit_factor | 0.6473 |
| net_win_rate | 0.4654 |
| gross_profit_factor | 0.8502 |
| gross_win_rate | 0.4654 |
| sharpe_ratio | -2.8451 |
| sortino_ratio | -0.8719 |
| max_drawdown | 0.6532 |
| cagr | -0.3297 |
| net_avg_win | 54.1162 |
| net_avg_loss | -72.7674 |
| avg_hold_time_bars | 5.5195 |
| exposure | 0.1159 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
