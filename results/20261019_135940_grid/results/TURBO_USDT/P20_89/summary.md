# EMA Hourly Continuation — TURBO/USDT P20_89

**Symbol:** TURBO/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 641 |
| net_profit_factor | 0.6442 |
| net_win_rate | 0.4680 |
| gross_profit_factor | 0.9086 |
| gross_win_rate | 0.4711 |
| sharpe_ratio | -4.3247 |
| sortino_ratio | -1.6901 |
| max_drawdown | 0.8221 |
| cagr | -0.5510 |
| net_avg_win | 49.0607 |
| net_avg_loss | -66.9978 |
| avg_hold_time_bars | 10.6459 |
| exposure | 0.3723 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
