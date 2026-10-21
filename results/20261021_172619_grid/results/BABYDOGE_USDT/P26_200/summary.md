# EMA Hourly Continuation — BABYDOGE/USDT P26_200

**Symbol:** BABYDOGE/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 60 |
| net_profit_factor | 1.1424 |
| net_win_rate | 0.5500 |
| gross_profit_factor | 1.2091 |
| gross_win_rate | 0.5500 |
| sharpe_ratio | 0.3499 |
| sortino_ratio | 0.0394 |
| max_drawdown | 0.0665 |
| cagr | 0.0160 |
| net_avg_win | 99.3419 |
| net_avg_loss | -106.2853 |
| avg_hold_time_bars | 77.8833 |
| exposure | 0.2115 |

Decision label: exploratory signal


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
