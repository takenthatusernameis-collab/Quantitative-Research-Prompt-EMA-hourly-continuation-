# EMA Hourly Continuation — MOVR/USDT P21_26

**Symbol:** MOVR/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 239 |
| net_profit_factor | 0.5763 |
| net_win_rate | 0.4603 |
| gross_profit_factor | 0.8286 |
| gross_win_rate | 0.4603 |
| sharpe_ratio | -2.5124 |
| sortino_ratio | -0.5555 |
| max_drawdown | 0.5176 |
| cagr | -0.2251 |
| net_avg_win | 58.4779 |
| net_avg_loss | -86.5304 |
| avg_hold_time_bars | 4.8368 |
| exposure | 0.0525 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
