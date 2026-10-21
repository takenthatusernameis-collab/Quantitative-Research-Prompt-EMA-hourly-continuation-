# EMA Hourly Continuation — TURBO/USDT P8_50

**Symbol:** TURBO/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 578 |
| net_profit_factor | 0.8398 |
| net_win_rate | 0.5017 |
| gross_profit_factor | 1.0228 |
| gross_win_rate | 0.5017 |
| sharpe_ratio | -1.6368 |
| sortino_ratio | -0.6174 |
| max_drawdown | 0.5272 |
| cagr | -0.2493 |
| net_avg_win | 81.5805 |
| net_avg_loss | -97.8154 |
| avg_hold_time_bars | 12.7561 |
| exposure | 0.4022 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
