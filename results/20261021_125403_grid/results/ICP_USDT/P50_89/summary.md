# EMA Hourly Continuation — ICP/USDT P50_89

**Symbol:** ICP/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 331 |
| net_profit_factor | 0.7081 |
| net_win_rate | 0.4894 |
| gross_profit_factor | 0.9486 |
| gross_win_rate | 0.4894 |
| sharpe_ratio | -1.9156 |
| sortino_ratio | -0.4991 |
| max_drawdown | 0.4464 |
| cagr | -0.2042 |
| net_avg_win | 65.3678 |
| net_avg_loss | -88.4928 |
| avg_hold_time_bars | 7.5831 |
| exposure | 0.1141 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
