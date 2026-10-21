# EMA Hourly Continuation — POL/USDT P8_100

**Symbol:** POL/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 392 |
| net_profit_factor | 0.8421 |
| net_win_rate | 0.5153 |
| gross_profit_factor | 1.0484 |
| gross_win_rate | 0.5153 |
| sharpe_ratio | -1.0153 |
| sortino_ratio | -0.2884 |
| max_drawdown | 0.3670 |
| cagr | -0.1265 |
| net_avg_win | 76.0109 |
| net_avg_loss | -95.9681 |
| avg_hold_time_bars | 39.4464 |
| exposure | 0.7029 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
