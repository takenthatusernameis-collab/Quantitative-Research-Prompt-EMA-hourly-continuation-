# EMA Hourly Continuation — THETA/USDT P55_144

**Symbol:** THETA/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 337 |
| net_profit_factor | 0.8343 |
| net_win_rate | 0.5163 |
| gross_profit_factor | 1.0531 |
| gross_win_rate | 0.5163 |
| sharpe_ratio | -0.9701 |
| sortino_ratio | -0.2562 |
| max_drawdown | 0.2801 |
| cagr | -0.1128 |
| net_avg_win | 75.0914 |
| net_avg_loss | -96.0794 |
| avg_hold_time_bars | 14.7864 |
| exposure | 0.2265 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
