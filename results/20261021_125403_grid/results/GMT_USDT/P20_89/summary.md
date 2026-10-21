# EMA Hourly Continuation — GMT/USDT P20_89

**Symbol:** GMT/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 515 |
| net_profit_factor | 0.6750 |
| net_win_rate | 0.4524 |
| gross_profit_factor | 0.8500 |
| gross_win_rate | 0.4524 |
| sharpe_ratio | -3.0025 |
| sortino_ratio | -0.9677 |
| max_drawdown | 0.6963 |
| cagr | -0.3596 |
| net_avg_win | 60.0237 |
| net_avg_loss | -73.4740 |
| avg_hold_time_bars | 14.5786 |
| exposure | 0.3413 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
