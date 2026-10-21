# EMA Hourly Continuation — RENDER/USDT P20_34

**Symbol:** RENDER/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 254 |
| net_profit_factor | 0.6630 |
| net_win_rate | 0.4646 |
| gross_profit_factor | 0.8769 |
| gross_win_rate | 0.4646 |
| sharpe_ratio | -2.2505 |
| sortino_ratio | -0.5512 |
| max_drawdown | 0.4340 |
| cagr | -0.2228 |
| net_avg_win | 70.0529 |
| net_avg_loss | -91.6783 |
| avg_hold_time_bars | 5.6378 |
| exposure | 0.0756 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
