# EMA Hourly Continuation — WEMIX/USDT P89_200

**Symbol:** WEMIX/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 623 |
| net_profit_factor | 0.3622 |
| net_win_rate | 0.3323 |
| gross_profit_factor | 0.5643 |
| gross_win_rate | 0.3403 |
| sharpe_ratio | -8.7013 |
| sortino_ratio | -3.0801 |
| max_drawdown | 0.9774 |
| cagr | -0.7782 |
| net_avg_win | 26.8105 |
| net_avg_loss | -36.8318 |
| avg_hold_time_bars | 8.9230 |
| exposure | 0.2527 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
