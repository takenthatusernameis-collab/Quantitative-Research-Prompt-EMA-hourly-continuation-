# EMA Hourly Continuation — DEXE/USDT P8_200

**Symbol:** DEXE/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 354 |
| net_profit_factor | 0.7187 |
| net_win_rate | 0.4915 |
| gross_profit_factor | 0.9494 |
| gross_win_rate | 0.4972 |
| sharpe_ratio | -1.7594 |
| sortino_ratio | -0.4680 |
| max_drawdown | 0.5015 |
| cagr | -0.1993 |
| net_avg_win | 62.8245 |
| net_avg_loss | -84.4982 |
| avg_hold_time_bars | 50.8136 |
| exposure | 0.8176 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
