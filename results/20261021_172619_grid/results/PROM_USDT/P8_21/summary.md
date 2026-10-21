# EMA Hourly Continuation — PROM/USDT P8_21

**Symbol:** PROM/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 682 |
| net_profit_factor | 0.5456 |
| net_win_rate | 0.4531 |
| gross_profit_factor | 0.8291 |
| gross_win_rate | 0.4531 |
| sharpe_ratio | -4.8376 |
| sortino_ratio | -1.8007 |
| max_drawdown | 0.8802 |
| cagr | -0.5661 |
| net_avg_win | 34.0891 |
| net_avg_loss | -51.7554 |
| avg_hold_time_bars | 6.4032 |
| exposure | 0.1985 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
