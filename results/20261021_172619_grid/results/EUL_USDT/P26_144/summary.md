# EMA Hourly Continuation — EUL/USDT P26_144

**Symbol:** EUL/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 377 |
| net_profit_factor | 0.7225 |
| net_win_rate | 0.4695 |
| gross_profit_factor | 0.8709 |
| gross_win_rate | 0.4695 |
| sharpe_ratio | -1.8627 |
| sortino_ratio | -0.5138 |
| max_drawdown | 0.4701 |
| cagr | -0.2108 |
| net_avg_win | 65.9140 |
| net_avg_loss | -80.7383 |
| avg_hold_time_bars | 24.2679 |
| exposure | 0.4159 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
