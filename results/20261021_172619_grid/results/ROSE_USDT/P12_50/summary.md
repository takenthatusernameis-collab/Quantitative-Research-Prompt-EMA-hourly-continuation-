# EMA Hourly Continuation — ROSE/USDT P12_50

**Symbol:** ROSE/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 642 |
| net_profit_factor | 0.7895 |
| net_win_rate | 0.4969 |
| gross_profit_factor | 0.9890 |
| gross_win_rate | 0.4969 |
| sharpe_ratio | -1.9696 |
| sortino_ratio | -0.7141 |
| max_drawdown | 0.5922 |
| cagr | -0.2804 |
| net_avg_win | 66.1257 |
| net_avg_loss | -82.7191 |
| avg_hold_time_bars | 11.1558 |
| exposure | 0.3255 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
