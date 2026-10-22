# EMA Hourly Continuation — SKL/USDT P8_89

**Symbol:** SKL/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 499 |
| net_profit_factor | 0.8406 |
| net_win_rate | 0.5050 |
| gross_profit_factor | 1.0101 |
| gross_win_rate | 0.5050 |
| sharpe_ratio | -1.2175 |
| sortino_ratio | -0.3894 |
| max_drawdown | 0.4588 |
| cagr | -0.1664 |
| net_avg_win | 76.7985 |
| net_avg_loss | -93.2062 |
| avg_hold_time_bars | 28.9559 |
| exposure | 0.6568 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
