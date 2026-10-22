# EMA Hourly Continuation — 1INCH/USDT P50_100

**Symbol:** 1INCH/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 668 |
| net_profit_factor | 0.4376 |
| net_win_rate | 0.4326 |
| gross_profit_factor | 0.7985 |
| gross_win_rate | 0.4446 |
| sharpe_ratio | -6.9639 |
| sortino_ratio | -2.5252 |
| max_drawdown | 0.9606 |
| cagr | -0.7220 |
| net_avg_win | 25.8373 |
| net_avg_loss | -45.0269 |
| avg_hold_time_bars | 5.8952 |
| exposure | 0.1790 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
