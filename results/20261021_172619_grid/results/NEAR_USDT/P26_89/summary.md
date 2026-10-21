# EMA Hourly Continuation — NEAR/USDT P26_89

**Symbol:** NEAR/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 428 |
| net_profit_factor | 0.8182 |
| net_win_rate | 0.5023 |
| gross_profit_factor | 1.0013 |
| gross_win_rate | 0.5023 |
| sharpe_ratio | -1.2710 |
| sortino_ratio | -0.3768 |
| max_drawdown | 0.4064 |
| cagr | -0.1607 |
| net_avg_win | 74.5310 |
| net_avg_loss | -91.9439 |
| avg_hold_time_bars | 14.3715 |
| exposure | 0.2796 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
