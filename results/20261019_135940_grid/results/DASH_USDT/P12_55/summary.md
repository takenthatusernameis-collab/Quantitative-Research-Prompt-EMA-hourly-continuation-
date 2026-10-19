# EMA Hourly Continuation — DASH/USDT P12_55

**Symbol:** DASH/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1046 |
| net_profit_factor | 0.4776 |
| net_win_rate | 0.4608 |
| gross_profit_factor | 0.9809 |
| gross_win_rate | 0.4771 |
| sharpe_ratio | -6.6686 |
| sortino_ratio | -3.0221 |
| max_drawdown | 0.9760 |
| cagr | -0.7722 |
| net_avg_win | 18.5076 |
| net_avg_loss | -33.1154 |
| avg_hold_time_bars | 7.8212 |
| exposure | 0.3719 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
