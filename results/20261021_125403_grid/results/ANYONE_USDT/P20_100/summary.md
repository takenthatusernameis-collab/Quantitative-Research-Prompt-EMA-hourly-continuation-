# EMA Hourly Continuation — ANYONE/USDT P20_100

**Symbol:** ANYONE/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 442 |
| net_profit_factor | 0.7080 |
| net_win_rate | 0.4525 |
| gross_profit_factor | 0.8114 |
| gross_win_rate | 0.4525 |
| sharpe_ratio | -2.3225 |
| sortino_ratio | -0.7283 |
| max_drawdown | 0.5457 |
| cagr | -0.2860 |
| net_avg_win | 64.5805 |
| net_avg_loss | -75.3860 |
| avg_hold_time_bars | 16.9819 |
| exposure | 0.3793 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
