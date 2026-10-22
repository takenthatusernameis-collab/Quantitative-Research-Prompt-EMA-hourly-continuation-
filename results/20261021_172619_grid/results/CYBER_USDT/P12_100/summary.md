# EMA Hourly Continuation — CYBER/USDT P12_100

**Symbol:** CYBER/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 528 |
| net_profit_factor | 0.8323 |
| net_win_rate | 0.5076 |
| gross_profit_factor | 1.0223 |
| gross_win_rate | 0.5076 |
| sharpe_ratio | -1.3070 |
| sortino_ratio | -0.4304 |
| max_drawdown | 0.4073 |
| cagr | -0.1824 |
| net_avg_win | 73.5121 |
| net_avg_loss | -91.0409 |
| avg_hold_time_bars | 23.2860 |
| exposure | 0.5589 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
