# EMA Hourly Continuation — ETHFI/USDT P8_20

**Symbol:** ETHFI/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 473 |
| net_profit_factor | 0.8542 |
| net_win_rate | 0.5201 |
| gross_profit_factor | 1.0822 |
| gross_win_rate | 0.5201 |
| sharpe_ratio | -1.0794 |
| sortino_ratio | -0.3381 |
| max_drawdown | 0.3960 |
| cagr | -0.1465 |
| net_avg_win | 78.1963 |
| net_avg_loss | -99.1998 |
| avg_hold_time_bars | 5.3002 |
| exposure | 0.1140 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
