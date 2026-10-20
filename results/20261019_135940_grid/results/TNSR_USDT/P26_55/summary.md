# EMA Hourly Continuation — TNSR/USDT P26_55

**Symbol:** TNSR/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 895 |
| net_profit_factor | 0.6022 |
| net_win_rate | 0.4682 |
| gross_profit_factor | 0.9332 |
| gross_win_rate | 0.4793 |
| sharpe_ratio | -5.6027 |
| sortino_ratio | -2.3600 |
| max_drawdown | 0.9466 |
| cagr | -0.6778 |
| net_avg_win | 34.0580 |
| net_avg_loss | -49.7810 |
| avg_hold_time_bars | 4.8480 |
| exposure | 0.1964 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
