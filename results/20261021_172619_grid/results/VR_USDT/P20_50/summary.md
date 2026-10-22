# EMA Hourly Continuation — VR/USDT P20_50

**Symbol:** VR/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 353 |
| net_profit_factor | 0.6320 |
| net_win_rate | 0.4561 |
| gross_profit_factor | 0.8498 |
| gross_win_rate | 0.4561 |
| sharpe_ratio | -2.8837 |
| sortino_ratio | -0.7684 |
| max_drawdown | 0.5974 |
| cagr | -0.2995 |
| net_avg_win | 63.0493 |
| net_avg_loss | -83.6485 |
| avg_hold_time_bars | 12.0397 |
| exposure | 0.1932 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
