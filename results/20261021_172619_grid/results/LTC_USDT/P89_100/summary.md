# EMA Hourly Continuation — LTC/USDT P89_100

**Symbol:** LTC/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 82 |
| net_profit_factor | 0.5952 |
| net_win_rate | 0.4878 |
| gross_profit_factor | 0.9327 |
| gross_win_rate | 0.4878 |
| sharpe_ratio | -1.3758 |
| sortino_ratio | -0.1793 |
| max_drawdown | 0.1888 |
| cagr | -0.0790 |
| net_avg_win | 68.6086 |
| net_avg_loss | -109.7757 |
| avg_hold_time_bars | 6.9512 |
| exposure | 0.0259 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
