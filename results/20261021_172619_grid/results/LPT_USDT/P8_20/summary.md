# EMA Hourly Continuation — LPT/USDT P8_20

**Symbol:** LPT/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 649 |
| net_profit_factor | 0.7127 |
| net_win_rate | 0.5039 |
| gross_profit_factor | 1.0111 |
| gross_win_rate | 0.5039 |
| sharpe_ratio | -2.9844 |
| sortino_ratio | -1.0920 |
| max_drawdown | 0.7226 |
| cagr | -0.3935 |
| net_avg_win | 54.2374 |
| net_avg_loss | -77.2880 |
| avg_hold_time_bars | 4.9291 |
| exposure | 0.1454 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
