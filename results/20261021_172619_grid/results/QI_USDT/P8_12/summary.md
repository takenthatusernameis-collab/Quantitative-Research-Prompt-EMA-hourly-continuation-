# EMA Hourly Continuation — QI/USDT P8_12

**Symbol:** QI/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 485 |
| net_profit_factor | 0.6326 |
| net_win_rate | 0.4990 |
| gross_profit_factor | 0.9965 |
| gross_win_rate | 0.5010 |
| sharpe_ratio | -3.1704 |
| sortino_ratio | -0.9994 |
| max_drawdown | 0.6988 |
| cagr | -0.3686 |
| net_avg_win | 48.8436 |
| net_avg_loss | -76.8958 |
| avg_hold_time_bars | 5.5979 |
| exposure | 0.1229 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
