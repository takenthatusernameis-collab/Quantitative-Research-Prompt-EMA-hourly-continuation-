# EMA Hourly Continuation — PUFFER/USDT P50_55

**Symbol:** PUFFER/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 608 |
| net_profit_factor | 0.3528 |
| net_win_rate | 0.3865 |
| gross_profit_factor | 0.8303 |
| gross_win_rate | 0.4276 |
| sharpe_ratio | -9.5798 |
| sortino_ratio | -3.7560 |
| max_drawdown | 0.9804 |
| cagr | -0.8575 |
| net_avg_win | 22.7386 |
| net_avg_loss | -40.6092 |
| avg_hold_time_bars | 2.7780 |
| exposure | 0.0956 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
