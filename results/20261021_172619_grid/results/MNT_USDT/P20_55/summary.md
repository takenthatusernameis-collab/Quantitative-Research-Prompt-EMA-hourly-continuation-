# EMA Hourly Continuation — MNT/USDT P20_55

**Symbol:** MNT/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 519 |
| net_profit_factor | 0.6855 |
| net_win_rate | 0.5048 |
| gross_profit_factor | 0.9921 |
| gross_win_rate | 0.5048 |
| sharpe_ratio | -2.5307 |
| sortino_ratio | -0.8274 |
| max_drawdown | 0.6308 |
| cagr | -0.3155 |
| net_avg_win | 51.0799 |
| net_avg_loss | -75.9647 |
| avg_hold_time_bars | 9.8882 |
| exposure | 0.2333 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
