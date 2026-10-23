# EMA Hourly Continuation — FLUX/USDT P26_34

**Symbol:** FLUX/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1056 |
| net_profit_factor | 0.2773 |
| net_win_rate | 0.4006 |
| gross_profit_factor | 0.7793 |
| gross_win_rate | 0.4337 |
| sharpe_ratio | -11.7776 |
| sortino_ratio | -5.5275 |
| max_drawdown | 0.9992 |
| cagr | -0.9415 |
| net_avg_win | 9.0640 |
| net_avg_loss | -21.8421 |
| avg_hold_time_bars | 1.8494 |
| exposure | 0.0888 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
