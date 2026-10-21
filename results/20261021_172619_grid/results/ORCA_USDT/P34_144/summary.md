# EMA Hourly Continuation — ORCA/USDT P34_144

**Symbol:** ORCA/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 385 |
| net_profit_factor | 0.7023 |
| net_win_rate | 0.4805 |
| gross_profit_factor | 0.8912 |
| gross_win_rate | 0.4805 |
| sharpe_ratio | -2.0261 |
| sortino_ratio | -0.5652 |
| max_drawdown | 0.5304 |
| cagr | -0.2298 |
| net_avg_win | 61.3101 |
| net_avg_loss | -80.7569 |
| avg_hold_time_bars | 22.8052 |
| exposure | 0.3991 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
