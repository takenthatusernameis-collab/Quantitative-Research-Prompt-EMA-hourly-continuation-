# EMA Hourly Continuation — CSPR/USDT P20_144

**Symbol:** CSPR/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 477 |
| net_profit_factor | 0.6660 |
| net_win_rate | 0.4549 |
| gross_profit_factor | 0.8216 |
| gross_win_rate | 0.4549 |
| sharpe_ratio | -2.6476 |
| sortino_ratio | -0.8203 |
| max_drawdown | 0.6428 |
| cagr | -0.3149 |
| net_avg_win | 56.3281 |
| net_avg_loss | -70.5935 |
| avg_hold_time_bars | 21.6834 |
| exposure | 0.4701 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
