# EMA Hourly Continuation — LUNA/USDT P12_26

**Symbol:** LUNA/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 396 |
| net_profit_factor | 0.6397 |
| net_win_rate | 0.4596 |
| gross_profit_factor | 0.8857 |
| gross_win_rate | 0.4596 |
| sharpe_ratio | -3.0520 |
| sortino_ratio | -0.8676 |
| max_drawdown | 0.6357 |
| cagr | -0.3287 |
| net_avg_win | 61.6844 |
| net_avg_loss | -82.0125 |
| avg_hold_time_bars | 5.4924 |
| exposure | 0.0989 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
