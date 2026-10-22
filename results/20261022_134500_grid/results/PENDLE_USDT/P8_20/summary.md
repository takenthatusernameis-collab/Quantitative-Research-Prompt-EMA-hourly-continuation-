# EMA Hourly Continuation — PENDLE/USDT P8_20

**Symbol:** PENDLE/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1644 |
| net_profit_factor | 0.4386 |
| net_win_rate | 0.4313 |
| gross_profit_factor | 0.8546 |
| gross_win_rate | 0.4465 |
| sharpe_ratio | -11.0305 |
| sortino_ratio | -6.3083 |
| max_drawdown | 0.9996 |
| cagr | -0.9560 |
| net_avg_win | 11.0149 |
| net_avg_loss | -19.0435 |
| avg_hold_time_bars | 2.8990 |
| exposure | 0.2166 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
