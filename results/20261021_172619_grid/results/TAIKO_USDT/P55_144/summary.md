# EMA Hourly Continuation — TAIKO/USDT P55_144

**Symbol:** TAIKO/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 303 |
| net_profit_factor | 0.7709 |
| net_win_rate | 0.4983 |
| gross_profit_factor | 0.9920 |
| gross_win_rate | 0.4983 |
| sharpe_ratio | -1.4795 |
| sortino_ratio | -0.3793 |
| max_drawdown | 0.3685 |
| cagr | -0.1598 |
| net_avg_win | 75.5048 |
| net_avg_loss | -97.3007 |
| avg_hold_time_bars | 14.8317 |
| exposure | 0.2159 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
