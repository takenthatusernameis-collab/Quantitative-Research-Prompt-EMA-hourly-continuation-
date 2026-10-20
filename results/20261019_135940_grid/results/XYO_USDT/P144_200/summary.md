# EMA Hourly Continuation — XYO/USDT P144_200

**Symbol:** XYO/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 528 |
| net_profit_factor | 0.4093 |
| net_win_rate | 0.4110 |
| gross_profit_factor | 0.7963 |
| gross_win_rate | 0.4280 |
| sharpe_ratio | -6.9500 |
| sortino_ratio | -2.2582 |
| max_drawdown | 0.9458 |
| cagr | -0.6831 |
| net_avg_win | 30.1751 |
| net_avg_loss | -51.4375 |
| avg_hold_time_bars | 4.4754 |
| exposure | 0.1069 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
