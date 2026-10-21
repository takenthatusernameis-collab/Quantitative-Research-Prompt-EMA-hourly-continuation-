# EMA Hourly Continuation — MNT/USDT P12_144

**Symbol:** MNT/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 316 |
| net_profit_factor | 0.9470 |
| net_win_rate | 0.5411 |
| gross_profit_factor | 1.1708 |
| gross_win_rate | 0.5411 |
| sharpe_ratio | -0.2497 |
| sortino_ratio | -0.0642 |
| max_drawdown | 0.1669 |
| cagr | -0.0339 |
| net_avg_win | 86.6688 |
| net_avg_loss | -107.9270 |
| avg_hold_time_bars | 49.5981 |
| exposure | 0.7124 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
