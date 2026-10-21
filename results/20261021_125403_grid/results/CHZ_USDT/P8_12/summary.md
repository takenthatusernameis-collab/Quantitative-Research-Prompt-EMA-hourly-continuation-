# EMA Hourly Continuation — CHZ/USDT P8_12

**Symbol:** CHZ/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 235 |
| net_profit_factor | 0.7284 |
| net_win_rate | 0.5149 |
| gross_profit_factor | 1.0577 |
| gross_win_rate | 0.5149 |
| sharpe_ratio | -1.4944 |
| sortino_ratio | -0.3304 |
| max_drawdown | 0.3307 |
| cagr | -0.1399 |
| net_avg_win | 69.8339 |
| net_avg_loss | -101.7641 |
| avg_hold_time_bars | 4.8638 |
| exposure | 0.0520 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
