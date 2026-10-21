# EMA Hourly Continuation — TNSR/USDT P12_50

**Symbol:** TNSR/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 671 |
| net_profit_factor | 0.8339 |
| net_win_rate | 0.5037 |
| gross_profit_factor | 1.0427 |
| gross_win_rate | 0.5037 |
| sharpe_ratio | -1.7952 |
| sortino_ratio | -0.6641 |
| max_drawdown | 0.5969 |
| cagr | -0.2659 |
| net_avg_win | 80.4355 |
| net_avg_loss | -97.9042 |
| avg_hold_time_bars | 10.7407 |
| exposure | 0.3262 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
