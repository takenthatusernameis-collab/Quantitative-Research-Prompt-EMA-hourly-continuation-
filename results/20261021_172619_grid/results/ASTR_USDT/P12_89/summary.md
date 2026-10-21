# EMA Hourly Continuation — ASTR/USDT P12_89

**Symbol:** ASTR/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 536 |
| net_profit_factor | 0.8192 |
| net_win_rate | 0.5168 |
| gross_profit_factor | 1.0714 |
| gross_win_rate | 0.5168 |
| sharpe_ratio | -1.5163 |
| sortino_ratio | -0.5016 |
| max_drawdown | 0.4721 |
| cagr | -0.2088 |
| net_avg_win | 72.9687 |
| net_avg_loss | -95.2632 |
| avg_hold_time_bars | 22.4869 |
| exposure | 0.5454 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
