# EMA Hourly Continuation — MANTA/USDT P8_12

**Symbol:** MANTA/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 348 |
| net_profit_factor | 0.6893 |
| net_win_rate | 0.4943 |
| gross_profit_factor | 0.9989 |
| gross_win_rate | 0.4971 |
| sharpe_ratio | -2.3344 |
| sortino_ratio | -0.6250 |
| max_drawdown | 0.5311 |
| cagr | -0.2487 |
| net_avg_win | 66.0859 |
| net_avg_loss | -93.6928 |
| avg_hold_time_bars | 4.8793 |
| exposure | 0.0772 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
