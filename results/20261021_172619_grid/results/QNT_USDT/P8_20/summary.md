# EMA Hourly Continuation — QNT/USDT P8_20

**Symbol:** QNT/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 475 |
| net_profit_factor | 0.7580 |
| net_win_rate | 0.5305 |
| gross_profit_factor | 1.1109 |
| gross_win_rate | 0.5305 |
| sharpe_ratio | -1.7942 |
| sortino_ratio | -0.5654 |
| max_drawdown | 0.5217 |
| cagr | -0.2272 |
| net_avg_win | 59.2364 |
| net_avg_loss | -88.3092 |
| avg_hold_time_bars | 5.5537 |
| exposure | 0.1199 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
