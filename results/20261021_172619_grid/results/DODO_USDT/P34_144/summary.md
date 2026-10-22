# EMA Hourly Continuation — DODO/USDT P34_144

**Symbol:** DODO/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 415 |
| net_profit_factor | 0.7322 |
| net_win_rate | 0.4699 |
| gross_profit_factor | 0.9067 |
| gross_win_rate | 0.4699 |
| sharpe_ratio | -2.1615 |
| sortino_ratio | -0.6251 |
| max_drawdown | 0.5452 |
| cagr | -0.2501 |
| net_avg_win | 72.3573 |
| net_avg_loss | -87.5970 |
| avg_hold_time_bars | 18.7952 |
| exposure | 0.3530 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
