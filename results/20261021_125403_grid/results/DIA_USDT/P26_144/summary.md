# EMA Hourly Continuation — DIA/USDT P26_144

**Symbol:** DIA/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 416 |
| net_profit_factor | 0.7855 |
| net_win_rate | 0.4976 |
| gross_profit_factor | 0.9777 |
| gross_win_rate | 0.4976 |
| sharpe_ratio | -1.5094 |
| sortino_ratio | -0.4393 |
| max_drawdown | 0.4761 |
| cagr | -0.1843 |
| net_avg_win | 71.0929 |
| net_avg_loss | -89.6396 |
| avg_hold_time_bars | 24.0457 |
| exposure | 0.4526 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
