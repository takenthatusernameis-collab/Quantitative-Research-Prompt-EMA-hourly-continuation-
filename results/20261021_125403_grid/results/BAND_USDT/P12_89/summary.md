# EMA Hourly Continuation — BAND/USDT P12_89

**Symbol:** BAND/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 527 |
| net_profit_factor | 0.7912 |
| net_win_rate | 0.4953 |
| gross_profit_factor | 1.0076 |
| gross_win_rate | 0.4991 |
| sharpe_ratio | -1.8751 |
| sortino_ratio | -0.6128 |
| max_drawdown | 0.5731 |
| cagr | -0.2473 |
| net_avg_win | 74.2623 |
| net_avg_loss | -92.1004 |
| avg_hold_time_bars | 22.1404 |
| exposure | 0.5280 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
