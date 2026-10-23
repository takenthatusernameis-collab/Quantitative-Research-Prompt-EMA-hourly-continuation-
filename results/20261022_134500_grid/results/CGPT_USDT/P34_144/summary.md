# EMA Hourly Continuation — CGPT/USDT P34_144

**Symbol:** CGPT/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 455 |
| net_profit_factor | 0.6621 |
| net_win_rate | 0.4703 |
| gross_profit_factor | 0.9368 |
| gross_win_rate | 0.4747 |
| sharpe_ratio | -3.0672 |
| sortino_ratio | -0.9225 |
| max_drawdown | 0.6715 |
| cagr | -0.3557 |
| net_avg_win | 61.2107 |
| net_avg_loss | -82.0883 |
| avg_hold_time_bars | 18.5912 |
| exposure | 0.3845 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
