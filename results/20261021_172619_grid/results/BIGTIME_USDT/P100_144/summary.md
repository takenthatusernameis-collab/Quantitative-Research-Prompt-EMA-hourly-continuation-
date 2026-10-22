# EMA Hourly Continuation — BIGTIME/USDT P100_144

**Symbol:** BIGTIME/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 269 |
| net_profit_factor | 0.6737 |
| net_win_rate | 0.4796 |
| gross_profit_factor | 0.9159 |
| gross_win_rate | 0.4796 |
| sharpe_ratio | -2.0553 |
| sortino_ratio | -0.4805 |
| max_drawdown | 0.4450 |
| cagr | -0.1972 |
| net_avg_win | 68.0696 |
| net_avg_loss | -93.1013 |
| avg_hold_time_bars | 6.4275 |
| exposure | 0.0782 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
