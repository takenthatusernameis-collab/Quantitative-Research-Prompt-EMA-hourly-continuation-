# EMA Hourly Continuation — XRP/USDT P8_12

**Symbol:** XRP/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1786 |
| net_profit_factor | 0.0997 |
| net_win_rate | 0.2968 |
| gross_profit_factor | 0.8344 |
| gross_win_rate | 0.3992 |
| sharpe_ratio | -22.1031 |
| sortino_ratio | -14.2318 |
| max_drawdown | 1.0000 |
| cagr | -0.9996 |
| net_avg_win | 2.0897 |
| net_avg_loss | -8.8436 |
| avg_hold_time_bars | 1.8561 |
| exposure | 0.1507 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
