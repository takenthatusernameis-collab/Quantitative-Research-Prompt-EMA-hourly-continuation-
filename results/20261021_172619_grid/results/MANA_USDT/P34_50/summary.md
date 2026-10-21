# EMA Hourly Continuation — MANA/USDT P34_50

**Symbol:** MANA/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 283 |
| net_profit_factor | 0.7213 |
| net_win_rate | 0.5124 |
| gross_profit_factor | 1.0587 |
| gross_win_rate | 0.5124 |
| sharpe_ratio | -1.7335 |
| sortino_ratio | -0.4206 |
| max_drawdown | 0.4211 |
| cagr | -0.1742 |
| net_avg_win | 68.1127 |
| net_avg_loss | -99.2238 |
| avg_hold_time_bars | 5.0954 |
| exposure | 0.0655 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
