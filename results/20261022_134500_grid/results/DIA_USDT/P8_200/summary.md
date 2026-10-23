# EMA Hourly Continuation — DIA/USDT P8_200

**Symbol:** DIA/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 363 |
| net_profit_factor | 0.7285 |
| net_win_rate | 0.4986 |
| gross_profit_factor | 1.0032 |
| gross_win_rate | 0.5096 |
| sharpe_ratio | -1.6745 |
| sortino_ratio | -0.4511 |
| max_drawdown | 0.4747 |
| cagr | -0.1926 |
| net_avg_win | 61.8284 |
| net_avg_loss | -84.4011 |
| avg_hold_time_bars | 48.8154 |
| exposure | 0.8018 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
