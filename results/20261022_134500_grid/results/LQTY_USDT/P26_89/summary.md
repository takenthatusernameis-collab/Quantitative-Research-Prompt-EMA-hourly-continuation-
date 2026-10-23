# EMA Hourly Continuation — LQTY/USDT P26_89

**Symbol:** LQTY/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 695 |
| net_profit_factor | 0.5998 |
| net_win_rate | 0.4619 |
| gross_profit_factor | 0.8936 |
| gross_win_rate | 0.4691 |
| sharpe_ratio | -4.4045 |
| sortino_ratio | -1.6416 |
| max_drawdown | 0.8646 |
| cagr | -0.5377 |
| net_avg_win | 40.0206 |
| net_avg_loss | -57.2683 |
| avg_hold_time_bars | 10.7252 |
| exposure | 0.3373 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
