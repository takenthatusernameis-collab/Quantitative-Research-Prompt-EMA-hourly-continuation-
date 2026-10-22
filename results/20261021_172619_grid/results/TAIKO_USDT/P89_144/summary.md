# EMA Hourly Continuation — TAIKO/USDT P89_144

**Symbol:** TAIKO/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 205 |
| net_profit_factor | 0.7535 |
| net_win_rate | 0.5073 |
| gross_profit_factor | 1.0206 |
| gross_win_rate | 0.5073 |
| sharpe_ratio | -1.2805 |
| sortino_ratio | -0.2707 |
| max_drawdown | 0.2824 |
| cagr | -0.1168 |
| net_avg_win | 75.1263 |
| net_avg_loss | -102.6679 |
| avg_hold_time_bars | 8.6341 |
| exposure | 0.0850 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
