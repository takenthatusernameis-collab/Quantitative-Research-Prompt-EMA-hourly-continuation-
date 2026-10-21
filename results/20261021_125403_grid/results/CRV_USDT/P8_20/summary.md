# EMA Hourly Continuation — CRV/USDT P8_20

**Symbol:** CRV/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 494 |
| net_profit_factor | 0.6974 |
| net_win_rate | 0.4919 |
| gross_profit_factor | 0.9400 |
| gross_win_rate | 0.4919 |
| sharpe_ratio | -2.3118 |
| sortino_ratio | -0.7363 |
| max_drawdown | 0.6002 |
| cagr | -0.2860 |
| net_avg_win | 54.1484 |
| net_avg_loss | -75.1688 |
| avg_hold_time_bars | 5.2955 |
| exposure | 0.1189 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
