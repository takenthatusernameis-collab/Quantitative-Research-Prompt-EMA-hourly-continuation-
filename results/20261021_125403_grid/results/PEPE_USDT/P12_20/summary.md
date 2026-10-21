# EMA Hourly Continuation — PEPE/USDT P12_20

**Symbol:** PEPE/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 236 |
| net_profit_factor | 0.8194 |
| net_win_rate | 0.5212 |
| gross_profit_factor | 1.0794 |
| gross_win_rate | 0.5212 |
| sharpe_ratio | -0.9258 |
| sortino_ratio | -0.2051 |
| max_drawdown | 0.2285 |
| cagr | -0.0903 |
| net_avg_win | 78.0436 |
| net_avg_loss | -103.6790 |
| avg_hold_time_bars | 4.2924 |
| exposure | 0.0460 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
