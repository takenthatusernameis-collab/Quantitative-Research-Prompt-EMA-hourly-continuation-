# EMA Hourly Continuation — XLM/USDT P50_144

**Symbol:** XLM/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 330 |
| net_profit_factor | 0.7669 |
| net_win_rate | 0.5121 |
| gross_profit_factor | 1.0445 |
| gross_win_rate | 0.5121 |
| sharpe_ratio | -1.4236 |
| sortino_ratio | -0.3718 |
| max_drawdown | 0.3987 |
| cagr | -0.1566 |
| net_avg_win | 67.7170 |
| net_avg_loss | -92.6910 |
| avg_hold_time_bars | 17.7212 |
| exposure | 0.2658 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
