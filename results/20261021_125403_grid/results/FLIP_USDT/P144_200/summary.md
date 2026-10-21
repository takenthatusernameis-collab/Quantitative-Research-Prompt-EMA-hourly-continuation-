# EMA Hourly Continuation — FLIP/USDT P144_200

**Symbol:** FLIP/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 186 |
| net_profit_factor | 0.4797 |
| net_win_rate | 0.4301 |
| gross_profit_factor | 0.7450 |
| gross_win_rate | 0.4355 |
| sharpe_ratio | -3.0301 |
| sortino_ratio | -0.5858 |
| max_drawdown | 0.5308 |
| cagr | -0.2391 |
| net_avg_win | 57.2324 |
| net_avg_loss | -90.0425 |
| avg_hold_time_bars | 13.5323 |
| exposure | 0.1144 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
