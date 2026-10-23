# EMA Hourly Continuation — TRADE/USDT P21_55

**Symbol:** TRADE/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 755 |
| net_profit_factor | 0.5374 |
| net_win_rate | 0.4384 |
| gross_profit_factor | 0.8533 |
| gross_win_rate | 0.4424 |
| sharpe_ratio | -6.1150 |
| sortino_ratio | -2.3320 |
| max_drawdown | 0.9510 |
| cagr | -0.6936 |
| net_avg_win | 33.2907 |
| net_avg_loss | -48.3641 |
| avg_hold_time_bars | 6.7391 |
| exposure | 0.2313 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
