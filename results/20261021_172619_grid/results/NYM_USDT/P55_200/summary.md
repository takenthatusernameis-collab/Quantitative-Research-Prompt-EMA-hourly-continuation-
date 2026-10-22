# EMA Hourly Continuation — NYM/USDT P55_200

**Symbol:** NYM/USDT  |  **P_fast:** 55  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 258 |
| net_profit_factor | 0.4561 |
| net_win_rate | 0.3915 |
| gross_profit_factor | 0.6487 |
| gross_win_rate | 0.3953 |
| sharpe_ratio | -3.7458 |
| sortino_ratio | -0.8509 |
| max_drawdown | 0.6397 |
| cagr | -0.3290 |
| net_avg_win | 52.5458 |
| net_avg_loss | -74.1102 |
| avg_hold_time_bars | 26.0930 |
| exposure | 0.3060 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
