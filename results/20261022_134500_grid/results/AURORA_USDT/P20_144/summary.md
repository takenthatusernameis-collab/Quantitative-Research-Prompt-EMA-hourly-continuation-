# EMA Hourly Continuation — AURORA/USDT P20_144

**Symbol:** AURORA/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 460 |
| net_profit_factor | 0.6264 |
| net_win_rate | 0.4609 |
| gross_profit_factor | 0.9666 |
| gross_win_rate | 0.4739 |
| sharpe_ratio | -3.7047 |
| sortino_ratio | -1.1072 |
| max_drawdown | 0.7594 |
| cagr | -0.4182 |
| net_avg_win | 58.7978 |
| net_avg_loss | -80.2389 |
| avg_hold_time_bars | 24.3391 |
| exposure | 0.5089 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
