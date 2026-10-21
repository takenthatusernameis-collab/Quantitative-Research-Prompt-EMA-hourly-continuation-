# EMA Hourly Continuation — XDC/USDT P12_20

**Symbol:** XDC/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 255 |
| net_profit_factor | 0.4098 |
| net_win_rate | 0.4235 |
| gross_profit_factor | 0.7041 |
| gross_win_rate | 0.4235 |
| sharpe_ratio | -4.0128 |
| sortino_ratio | -0.9225 |
| max_drawdown | 0.6588 |
| cagr | -0.3461 |
| net_avg_win | 42.1673 |
| net_avg_loss | -75.5969 |
| avg_hold_time_bars | 6.6314 |
| exposure | 0.0769 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
