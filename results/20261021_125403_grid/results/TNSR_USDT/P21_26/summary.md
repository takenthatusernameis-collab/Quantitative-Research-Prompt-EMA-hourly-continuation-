# EMA Hourly Continuation — TNSR/USDT P21_26

**Symbol:** TNSR/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 263 |
| net_profit_factor | 0.6026 |
| net_win_rate | 0.4677 |
| gross_profit_factor | 0.9001 |
| gross_win_rate | 0.4753 |
| sharpe_ratio | -2.6164 |
| sortino_ratio | -0.6061 |
| max_drawdown | 0.5235 |
| cagr | -0.2417 |
| net_avg_win | 61.9310 |
| net_avg_loss | -90.2974 |
| avg_hold_time_bars | 4.0114 |
| exposure | 0.0477 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
