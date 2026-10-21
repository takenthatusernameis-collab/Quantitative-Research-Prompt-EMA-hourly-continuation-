# EMA Hourly Continuation — T/USDT P21_55

**Symbol:** T/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 568 |
| net_profit_factor | 0.6813 |
| net_win_rate | 0.4982 |
| gross_profit_factor | 1.0208 |
| gross_win_rate | 0.4982 |
| sharpe_ratio | -3.1400 |
| sortino_ratio | -1.0679 |
| max_drawdown | 0.7254 |
| cagr | -0.3885 |
| net_avg_win | 53.6998 |
| net_avg_loss | -78.2655 |
| avg_hold_time_bars | 8.9384 |
| exposure | 0.2297 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
