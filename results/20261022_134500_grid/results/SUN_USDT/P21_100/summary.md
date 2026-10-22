# EMA Hourly Continuation — SUN/USDT P21_100

**Symbol:** SUN/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 596 |
| net_profit_factor | 0.3850 |
| net_win_rate | 0.3876 |
| gross_profit_factor | 0.7767 |
| gross_win_rate | 0.4346 |
| sharpe_ratio | -7.8408 |
| sortino_ratio | -2.6896 |
| max_drawdown | 0.9698 |
| cagr | -0.7488 |
| net_avg_win | 26.2637 |
| net_avg_loss | -43.1786 |
| avg_hold_time_bars | 16.3557 |
| exposure | 0.4411 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
