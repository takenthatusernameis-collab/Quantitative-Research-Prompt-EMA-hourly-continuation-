# EMA Hourly Continuation — LTC/USDT P8_100

**Symbol:** LTC/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 665 |
| net_profit_factor | 0.4626 |
| net_win_rate | 0.4376 |
| gross_profit_factor | 0.8763 |
| gross_win_rate | 0.4541 |
| sharpe_ratio | -6.3734 |
| sortino_ratio | -2.2954 |
| max_drawdown | 0.9477 |
| cagr | -0.6856 |
| net_avg_win | 27.9663 |
| net_avg_loss | -47.0352 |
| avg_hold_time_bars | 22.0331 |
| exposure | 0.6660 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
