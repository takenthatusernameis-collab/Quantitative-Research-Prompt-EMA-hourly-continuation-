# EMA Hourly Continuation — RUNE/USDT P144_200

**Symbol:** RUNE/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 176 |
| net_profit_factor | 0.7390 |
| net_win_rate | 0.5057 |
| gross_profit_factor | 1.0089 |
| gross_win_rate | 0.5057 |
| sharpe_ratio | -1.1727 |
| sortino_ratio | -0.2236 |
| max_drawdown | 0.2694 |
| cagr | -0.0968 |
| net_avg_win | 71.8159 |
| net_avg_loss | -99.4098 |
| avg_hold_time_bars | 8.0170 |
| exposure | 0.0641 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
