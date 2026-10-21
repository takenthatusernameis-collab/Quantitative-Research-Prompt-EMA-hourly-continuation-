# EMA Hourly Continuation — BCH/USDT P21_200

**Symbol:** BCH/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 233 |
| net_profit_factor | 0.7960 |
| net_win_rate | 0.4979 |
| gross_profit_factor | 0.9859 |
| gross_win_rate | 0.4979 |
| sharpe_ratio | -1.0733 |
| sortino_ratio | -0.2344 |
| max_drawdown | 0.2979 |
| cagr | -0.1028 |
| net_avg_win | 80.2152 |
| net_avg_loss | -99.9170 |
| avg_hold_time_bars | 63.1545 |
| exposure | 0.6689 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
