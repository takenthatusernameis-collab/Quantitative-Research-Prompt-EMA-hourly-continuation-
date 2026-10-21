# EMA Hourly Continuation — CFG/USDT P50_200

**Symbol:** CFG/USDT  |  **P_fast:** 50  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 343 |
| net_profit_factor | 0.8065 |
| net_win_rate | 0.4869 |
| gross_profit_factor | 0.9444 |
| gross_win_rate | 0.4869 |
| sharpe_ratio | -1.1901 |
| sortino_ratio | -0.3144 |
| max_drawdown | 0.3532 |
| cagr | -0.1358 |
| net_avg_win | 76.5796 |
| net_avg_loss | -90.0952 |
| avg_hold_time_bars | 21.9388 |
| exposure | 0.3420 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
