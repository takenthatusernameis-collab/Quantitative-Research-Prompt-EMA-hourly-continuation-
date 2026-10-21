# EMA Hourly Continuation — LTC/USDT P55_100

**Symbol:** LTC/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 310 |
| net_profit_factor | 0.5406 |
| net_win_rate | 0.4581 |
| gross_profit_factor | 0.8079 |
| gross_win_rate | 0.4581 |
| sharpe_ratio | -3.0598 |
| sortino_ratio | -0.7711 |
| max_drawdown | 0.6002 |
| cagr | -0.2976 |
| net_avg_win | 48.7466 |
| net_avg_loss | -76.2125 |
| avg_hold_time_bars | 9.1290 |
| exposure | 0.1286 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
