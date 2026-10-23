# EMA Hourly Continuation — ARKM/USDT P50_200

**Symbol:** ARKM/USDT  |  **P_fast:** 50  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 394 |
| net_profit_factor | 0.6758 |
| net_win_rate | 0.4772 |
| gross_profit_factor | 0.9042 |
| gross_win_rate | 0.4873 |
| sharpe_ratio | -2.2531 |
| sortino_ratio | -0.6287 |
| max_drawdown | 0.5504 |
| cagr | -0.2580 |
| net_avg_win | 58.4876 |
| net_avg_loss | -78.9791 |
| avg_hold_time_bars | 21.7208 |
| exposure | 0.3890 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
