# EMA Hourly Continuation — RAY/USDT P8_21

**Symbol:** RAY/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1613 |
| net_profit_factor | 0.5026 |
| net_win_rate | 0.4464 |
| gross_profit_factor | 0.9365 |
| gross_win_rate | 0.4613 |
| sharpe_ratio | -9.8897 |
| sortino_ratio | -5.5720 |
| max_drawdown | 0.9991 |
| cagr | -0.9386 |
| net_avg_win | 14.0208 |
| net_avg_loss | -22.4927 |
| avg_hold_time_bars | 3.2951 |
| exposure | 0.2416 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
