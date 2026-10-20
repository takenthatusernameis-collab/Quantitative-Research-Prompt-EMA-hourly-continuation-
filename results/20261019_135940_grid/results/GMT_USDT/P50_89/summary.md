# EMA Hourly Continuation — GMT/USDT P50_89

**Symbol:** GMT/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 685 |
| net_profit_factor | 0.4911 |
| net_win_rate | 0.4307 |
| gross_profit_factor | 0.8932 |
| gross_win_rate | 0.4438 |
| sharpe_ratio | -6.5952 |
| sortino_ratio | -2.4442 |
| max_drawdown | 0.9528 |
| cagr | -0.6970 |
| net_avg_win | 31.0832 |
| net_avg_loss | -47.8738 |
| avg_hold_time_bars | 4.4715 |
| exposure | 0.1392 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
