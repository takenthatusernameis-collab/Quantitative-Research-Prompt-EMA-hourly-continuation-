# EMA Hourly Continuation — PYTH/USDT P21_144

**Symbol:** PYTH/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 508 |
| net_profit_factor | 0.7531 |
| net_win_rate | 0.5020 |
| gross_profit_factor | 1.0399 |
| gross_win_rate | 0.5059 |
| sharpe_ratio | -2.0652 |
| sortino_ratio | -0.6582 |
| max_drawdown | 0.5715 |
| cagr | -0.2679 |
| net_avg_win | 64.9475 |
| net_avg_loss | -86.9251 |
| avg_hold_time_bars | 22.7795 |
| exposure | 0.5260 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
