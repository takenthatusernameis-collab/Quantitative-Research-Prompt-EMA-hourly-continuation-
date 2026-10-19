# EMA Hourly Continuation — FLOKI/USDT P50_89

**Symbol:** FLOKI/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 713 |
| net_profit_factor | 0.5741 |
| net_win_rate | 0.4741 |
| gross_profit_factor | 0.9543 |
| gross_win_rate | 0.4923 |
| sharpe_ratio | -5.0160 |
| sortino_ratio | -1.8976 |
| max_drawdown | 0.9023 |
| cagr | -0.5962 |
| net_avg_win | 35.7837 |
| net_avg_loss | -56.1849 |
| avg_hold_time_bars | 4.9088 |
| exposure | 0.1591 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
