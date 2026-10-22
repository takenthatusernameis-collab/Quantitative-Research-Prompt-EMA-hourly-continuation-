# EMA Hourly Continuation — WAVES/USDT P21_144

**Symbol:** WAVES/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 459 |
| net_profit_factor | 0.7539 |
| net_win_rate | 0.4967 |
| gross_profit_factor | 0.9823 |
| gross_win_rate | 0.4967 |
| sharpe_ratio | -1.9040 |
| sortino_ratio | -0.5835 |
| max_drawdown | 0.5313 |
| cagr | -0.2362 |
| net_avg_win | 66.0761 |
| net_avg_loss | -86.5070 |
| avg_hold_time_bars | 23.8148 |
| exposure | 0.4969 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
