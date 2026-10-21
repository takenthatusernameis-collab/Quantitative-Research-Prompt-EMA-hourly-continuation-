# EMA Hourly Continuation — BTC/USDT P8_20

**Symbol:** BTC/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 508 |
| net_profit_factor | 0.5343 |
| net_win_rate | 0.5098 |
| gross_profit_factor | 1.0215 |
| gross_win_rate | 0.5177 |
| sharpe_ratio | -3.9371 |
| sortino_ratio | -1.2063 |
| max_drawdown | 0.7951 |
| cagr | -0.4248 |
| net_avg_win | 35.1582 |
| net_avg_loss | -68.4425 |
| avg_hold_time_bars | 6.3445 |
| exposure | 0.1289 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
