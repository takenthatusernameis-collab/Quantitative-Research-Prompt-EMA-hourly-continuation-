# EMA Hourly Continuation — MOG/USDT P8_55

**Symbol:** MOG/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 902 |
| net_profit_factor | 0.6940 |
| net_win_rate | 0.4756 |
| gross_profit_factor | 0.9256 |
| gross_win_rate | 0.4812 |
| sharpe_ratio | -4.0425 |
| sortino_ratio | -1.7880 |
| max_drawdown | 0.8590 |
| cagr | -0.5728 |
| net_avg_win | 45.3705 |
| net_avg_loss | -59.2924 |
| avg_hold_time_bars | 11.2217 |
| exposure | 0.5032 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
