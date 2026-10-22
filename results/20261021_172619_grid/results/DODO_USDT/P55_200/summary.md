# EMA Hourly Continuation — DODO/USDT P55_200

**Symbol:** DODO/USDT  |  **P_fast:** 55  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 356 |
| net_profit_factor | 0.6271 |
| net_win_rate | 0.4326 |
| gross_profit_factor | 0.7700 |
| gross_win_rate | 0.4326 |
| sharpe_ratio | -2.8563 |
| sortino_ratio | -0.7594 |
| max_drawdown | 0.5987 |
| cagr | -0.2954 |
| net_avg_win | 64.0355 |
| net_avg_loss | -77.8536 |
| avg_hold_time_bars | 21.2725 |
| exposure | 0.3427 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
