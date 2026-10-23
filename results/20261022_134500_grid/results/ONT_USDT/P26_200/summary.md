# EMA Hourly Continuation — ONT/USDT P26_200

**Symbol:** ONT/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 420 |
| net_profit_factor | 0.5953 |
| net_win_rate | 0.4500 |
| gross_profit_factor | 0.8466 |
| gross_win_rate | 0.4571 |
| sharpe_ratio | -3.3666 |
| sortino_ratio | -0.9704 |
| max_drawdown | 0.6952 |
| cagr | -0.3683 |
| net_avg_win | 53.4044 |
| net_avg_loss | -73.3971 |
| avg_hold_time_bars | 28.7381 |
| exposure | 0.5462 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
