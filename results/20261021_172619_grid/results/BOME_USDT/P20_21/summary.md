# EMA Hourly Continuation — BOME/USDT P20_21

**Symbol:** BOME/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 132 |
| net_profit_factor | 0.7281 |
| net_win_rate | 0.4924 |
| gross_profit_factor | 0.9593 |
| gross_win_rate | 0.4924 |
| sharpe_ratio | -1.1115 |
| sortino_ratio | -0.1829 |
| max_drawdown | 0.2608 |
| cagr | -0.0808 |
| net_avg_win | 78.5318 |
| net_avg_loss | -104.6414 |
| avg_hold_time_bars | 4.5303 |
| exposure | 0.0272 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
