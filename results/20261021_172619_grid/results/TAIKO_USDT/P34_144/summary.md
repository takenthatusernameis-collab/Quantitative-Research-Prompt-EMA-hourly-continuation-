# EMA Hourly Continuation — TAIKO/USDT P34_144

**Symbol:** TAIKO/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 344 |
| net_profit_factor | 0.7399 |
| net_win_rate | 0.4797 |
| gross_profit_factor | 0.9250 |
| gross_win_rate | 0.4797 |
| sharpe_ratio | -1.8697 |
| sortino_ratio | -0.5081 |
| max_drawdown | 0.4432 |
| cagr | -0.2089 |
| net_avg_win | 73.6244 |
| net_avg_loss | -91.7209 |
| avg_hold_time_bars | 23.1047 |
| exposure | 0.3818 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
