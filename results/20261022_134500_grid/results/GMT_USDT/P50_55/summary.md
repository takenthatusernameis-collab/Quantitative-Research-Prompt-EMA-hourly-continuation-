# EMA Hourly Continuation — GMT/USDT P50_55

**Symbol:** GMT/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 820 |
| net_profit_factor | 0.2513 |
| net_win_rate | 0.3622 |
| gross_profit_factor | 0.8426 |
| gross_win_rate | 0.4110 |
| sharpe_ratio | -12.2516 |
| sortino_ratio | -5.1566 |
| max_drawdown | 0.9991 |
| cagr | -0.9377 |
| net_avg_win | 11.2896 |
| net_avg_loss | -25.5136 |
| avg_hold_time_bars | 1.8622 |
| exposure | 0.0694 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
