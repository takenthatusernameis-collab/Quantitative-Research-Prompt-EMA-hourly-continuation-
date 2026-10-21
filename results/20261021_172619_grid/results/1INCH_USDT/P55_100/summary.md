# EMA Hourly Continuation — 1INCH/USDT P55_100

**Symbol:** 1INCH/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 370 |
| net_profit_factor | 0.6490 |
| net_win_rate | 0.4730 |
| gross_profit_factor | 0.9117 |
| gross_win_rate | 0.4730 |
| sharpe_ratio | -2.7900 |
| sortino_ratio | -0.7684 |
| max_drawdown | 0.5980 |
| cagr | -0.2967 |
| net_avg_win | 61.9927 |
| net_avg_loss | -85.7254 |
| avg_hold_time_bars | 7.9000 |
| exposure | 0.1329 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
