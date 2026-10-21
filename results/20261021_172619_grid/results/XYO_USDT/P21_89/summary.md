# EMA Hourly Continuation — XYO/USDT P21_89

**Symbol:** XYO/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 520 |
| net_profit_factor | 0.6431 |
| net_win_rate | 0.4481 |
| gross_profit_factor | 0.8483 |
| gross_win_rate | 0.4481 |
| sharpe_ratio | -3.5721 |
| sortino_ratio | -1.1544 |
| max_drawdown | 0.7476 |
| cagr | -0.4128 |
| net_avg_win | 57.1456 |
| net_avg_loss | -72.1408 |
| avg_hold_time_bars | 14.3538 |
| exposure | 0.3378 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
