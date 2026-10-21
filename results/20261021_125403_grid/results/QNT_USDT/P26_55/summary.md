# EMA Hourly Continuation — QNT/USDT P26_55

**Symbol:** QNT/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 435 |
| net_profit_factor | 0.7040 |
| net_win_rate | 0.5057 |
| gross_profit_factor | 1.0113 |
| gross_win_rate | 0.5057 |
| sharpe_ratio | -2.2380 |
| sortino_ratio | -0.6716 |
| max_drawdown | 0.5739 |
| cagr | -0.2638 |
| net_avg_win | 58.0139 |
| net_avg_loss | -84.3194 |
| avg_hold_time_bars | 6.4092 |
| exposure | 0.1267 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
