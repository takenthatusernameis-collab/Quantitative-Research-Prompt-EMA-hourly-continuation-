# EMA Hourly Continuation — CETUS/USDT P12_26

**Symbol:** CETUS/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1397 |
| net_profit_factor | 0.5491 |
| net_win_rate | 0.4409 |
| gross_profit_factor | 1.0025 |
| gross_win_rate | 0.4624 |
| sharpe_ratio | -9.2809 |
| sortino_ratio | -4.8517 |
| max_drawdown | 0.9979 |
| cagr | -0.9110 |
| net_avg_win | 19.7255 |
| net_avg_loss | -28.3337 |
| avg_hold_time_bars | 3.0286 |
| exposure | 0.1915 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
