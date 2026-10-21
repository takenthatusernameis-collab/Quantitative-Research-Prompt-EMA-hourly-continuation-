# EMA Hourly Continuation — ALGO/USDT P26_144

**Symbol:** ALGO/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 376 |
| net_profit_factor | 0.9086 |
| net_win_rate | 0.5293 |
| gross_profit_factor | 1.1191 |
| gross_win_rate | 0.5293 |
| sharpe_ratio | -0.5823 |
| sortino_ratio | -0.1627 |
| max_drawdown | 0.2948 |
| cagr | -0.0756 |
| net_avg_win | 89.4804 |
| net_avg_loss | -110.7243 |
| avg_hold_time_bars | 26.0984 |
| exposure | 0.4460 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
