# EMA Hourly Continuation — STRK/USDT P100_200

**Symbol:** STRK/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 265 |
| net_profit_factor | 0.8246 |
| net_win_rate | 0.5019 |
| gross_profit_factor | 0.9952 |
| gross_win_rate | 0.5019 |
| sharpe_ratio | -0.9242 |
| sortino_ratio | -0.2156 |
| max_drawdown | 0.2732 |
| cagr | -0.0959 |
| net_avg_win | 79.0867 |
| net_avg_loss | -96.6357 |
| avg_hold_time_bars | 14.1170 |
| exposure | 0.1700 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
