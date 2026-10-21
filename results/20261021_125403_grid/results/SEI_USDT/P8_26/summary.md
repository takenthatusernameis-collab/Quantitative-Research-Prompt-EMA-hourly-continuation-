# EMA Hourly Continuation — SEI/USDT P8_26

**Symbol:** SEI/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 640 |
| net_profit_factor | 0.7683 |
| net_win_rate | 0.4984 |
| gross_profit_factor | 1.0025 |
| gross_win_rate | 0.4984 |
| sharpe_ratio | -2.2714 |
| sortino_ratio | -0.8238 |
| max_drawdown | 0.6341 |
| cagr | -0.3154 |
| net_avg_win | 63.8090 |
| net_avg_loss | -82.5344 |
| avg_hold_time_bars | 7.0234 |
| exposure | 0.2043 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
