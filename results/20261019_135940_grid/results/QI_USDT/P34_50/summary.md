# EMA Hourly Continuation — QI/USDT P34_50

**Symbol:** QI/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 854 |
| net_profit_factor | 0.4188 |
| net_win_rate | 0.4473 |
| gross_profit_factor | 0.9157 |
| gross_win_rate | 0.4813 |
| sharpe_ratio | -7.9243 |
| sortino_ratio | -3.3003 |
| max_drawdown | 0.9836 |
| cagr | -0.8016 |
| net_avg_win | 18.5429 |
| net_avg_loss | -35.8356 |
| avg_hold_time_bars | 2.9836 |
| exposure | 0.1153 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
