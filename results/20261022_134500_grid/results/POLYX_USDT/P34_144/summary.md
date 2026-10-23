# EMA Hourly Continuation — POLYX/USDT P34_144

**Symbol:** POLYX/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 470 |
| net_profit_factor | 0.6842 |
| net_win_rate | 0.4915 |
| gross_profit_factor | 0.9994 |
| gross_win_rate | 0.5021 |
| sharpe_ratio | -2.5701 |
| sortino_ratio | -0.7861 |
| max_drawdown | 0.6356 |
| cagr | -0.3108 |
| net_avg_win | 56.9456 |
| net_avg_loss | -80.4490 |
| avg_hold_time_bars | 19.5277 |
| exposure | 0.4172 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
