# EMA Hourly Continuation — XRP/USDT P55_200

**Symbol:** XRP/USDT  |  **P_fast:** 55  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 299 |
| net_profit_factor | 0.6532 |
| net_win_rate | 0.4816 |
| gross_profit_factor | 0.9056 |
| gross_win_rate | 0.4816 |
| sharpe_ratio | -2.1521 |
| sortino_ratio | -0.5319 |
| max_drawdown | 0.4848 |
| cagr | -0.2173 |
| net_avg_win | 60.1043 |
| net_avg_loss | -85.4844 |
| avg_hold_time_bars | 23.5418 |
| exposure | 0.3200 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
