# EMA Hourly Continuation — ASTR/USDT P26_55

**Symbol:** ASTR/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 816 |
| net_profit_factor | 0.4601 |
| net_win_rate | 0.4632 |
| gross_profit_factor | 0.9169 |
| gross_win_rate | 0.4865 |
| sharpe_ratio | -6.5777 |
| sortino_ratio | -2.6531 |
| max_drawdown | 0.9628 |
| cagr | -0.7271 |
| net_avg_win | 21.6933 |
| net_avg_loss | -40.6899 |
| avg_hold_time_bars | 5.4461 |
| exposure | 0.2011 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
