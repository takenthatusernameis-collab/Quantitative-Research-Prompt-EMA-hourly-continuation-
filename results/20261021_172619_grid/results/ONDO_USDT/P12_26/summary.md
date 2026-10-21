# EMA Hourly Continuation — ONDO/USDT P12_26

**Symbol:** ONDO/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 391 |
| net_profit_factor | 0.8015 |
| net_win_rate | 0.5166 |
| gross_profit_factor | 1.0653 |
| gross_win_rate | 0.5166 |
| sharpe_ratio | -1.3638 |
| sortino_ratio | -0.3885 |
| max_drawdown | 0.3858 |
| cagr | -0.1634 |
| net_avg_win | 72.2084 |
| net_avg_loss | -96.2827 |
| avg_hold_time_bars | 5.4629 |
| exposure | 0.0971 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
