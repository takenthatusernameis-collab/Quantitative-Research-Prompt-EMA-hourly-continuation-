# EMA Hourly Continuation — XDC/USDT P8_34

**Symbol:** XDC/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1424 |
| net_profit_factor | 0.2111 |
| net_win_rate | 0.3869 |
| gross_profit_factor | 0.5708 |
| gross_win_rate | 0.4389 |
| sharpe_ratio | -13.7038 |
| sortino_ratio | -7.3388 |
| max_drawdown | 0.9999 |
| cagr | -0.9791 |
| net_avg_win | 4.8554 |
| net_avg_loss | -14.5186 |
| avg_hold_time_bars | 4.8989 |
| exposure | 0.3171 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
