# EMA Hourly Continuation — CHZ/USDT P89_200

**Symbol:** CHZ/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 255 |
| net_profit_factor | 0.6901 |
| net_win_rate | 0.4667 |
| gross_profit_factor | 0.8693 |
| gross_win_rate | 0.4667 |
| sharpe_ratio | -1.8312 |
| sortino_ratio | -0.4164 |
| max_drawdown | 0.3947 |
| cagr | -0.1751 |
| net_avg_win | 71.7192 |
| net_avg_loss | -90.9389 |
| avg_hold_time_bars | 16.6784 |
| exposure | 0.1933 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
