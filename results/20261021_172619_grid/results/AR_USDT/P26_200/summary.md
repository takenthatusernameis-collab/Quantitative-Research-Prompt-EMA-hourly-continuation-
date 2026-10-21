# EMA Hourly Continuation — AR/USDT P26_200

**Symbol:** AR/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 313 |
| net_profit_factor | 0.7154 |
| net_win_rate | 0.4537 |
| gross_profit_factor | 0.8375 |
| gross_win_rate | 0.4537 |
| sharpe_ratio | -1.9391 |
| sortino_ratio | -0.4859 |
| max_drawdown | 0.4457 |
| cagr | -0.2012 |
| net_avg_win | 76.2980 |
| net_avg_loss | -88.5693 |
| avg_hold_time_bars | 41.3323 |
| exposure | 0.5880 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
