# EMA Hourly Continuation — VELO/USDT P89_200

**Symbol:** VELO/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 437 |
| net_profit_factor | 0.7019 |
| net_win_rate | 0.4874 |
| gross_profit_factor | 0.9729 |
| gross_win_rate | 0.4989 |
| sharpe_ratio | -2.2762 |
| sortino_ratio | -0.6767 |
| max_drawdown | 0.5714 |
| cagr | -0.2710 |
| net_avg_win | 60.5591 |
| net_avg_loss | -82.0459 |
| avg_hold_time_bars | 8.8719 |
| exposure | 0.1762 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
