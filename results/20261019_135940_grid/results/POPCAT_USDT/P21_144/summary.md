# EMA Hourly Continuation — POPCAT/USDT P21_144

**Symbol:** POPCAT/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 415 |
| net_profit_factor | 0.6216 |
| net_win_rate | 0.4506 |
| gross_profit_factor | 0.7977 |
| gross_win_rate | 0.4530 |
| sharpe_ratio | -3.1905 |
| sortino_ratio | -0.9826 |
| max_drawdown | 0.6429 |
| cagr | -0.3731 |
| net_avg_win | 55.8282 |
| net_avg_loss | -73.6597 |
| avg_hold_time_bars | 25.3373 |
| exposure | 0.5555 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
