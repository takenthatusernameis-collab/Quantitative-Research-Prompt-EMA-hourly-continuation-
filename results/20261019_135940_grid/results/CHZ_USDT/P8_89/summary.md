# EMA Hourly Continuation — CHZ/USDT P8_89

**Symbol:** CHZ/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 754 |
| net_profit_factor | 0.6033 |
| net_win_rate | 0.4867 |
| gross_profit_factor | 0.9721 |
| gross_win_rate | 0.4987 |
| sharpe_ratio | -4.0178 |
| sortino_ratio | -1.5426 |
| max_drawdown | 0.8591 |
| cagr | -0.5291 |
| net_avg_win | 35.1940 |
| net_avg_loss | -55.3171 |
| avg_hold_time_bars | 18.3793 |
| exposure | 0.6299 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
