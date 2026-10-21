# EMA Hourly Continuation — CRO/USDT P55_100

**Symbol:** CRO/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 309 |
| net_profit_factor | 0.6573 |
| net_win_rate | 0.4919 |
| gross_profit_factor | 0.9660 |
| gross_win_rate | 0.4919 |
| sharpe_ratio | -2.3011 |
| sortino_ratio | -0.5810 |
| max_drawdown | 0.5169 |
| cagr | -0.2330 |
| net_avg_win | 61.3782 |
| net_avg_loss | -90.4030 |
| avg_hold_time_bars | 9.3463 |
| exposure | 0.1313 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
