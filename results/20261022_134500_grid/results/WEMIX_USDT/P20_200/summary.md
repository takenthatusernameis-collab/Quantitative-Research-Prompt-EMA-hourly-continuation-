# EMA Hourly Continuation — WEMIX/USDT P20_200

**Symbol:** WEMIX/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 568 |
| net_profit_factor | 0.3708 |
| net_win_rate | 0.3275 |
| gross_profit_factor | 0.5583 |
| gross_win_rate | 0.3327 |
| sharpe_ratio | -8.2227 |
| sortino_ratio | -2.7569 |
| max_drawdown | 0.9693 |
| cagr | -0.7490 |
| net_avg_win | 30.7061 |
| net_avg_loss | -40.3160 |
| avg_hold_time_bars | 26.1937 |
| exposure | 0.6763 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
