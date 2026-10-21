# EMA Hourly Continuation — TRX/USDT P50_200

**Symbol:** TRX/USDT  |  **P_fast:** 50  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 267 |
| net_profit_factor | 0.5801 |
| net_win_rate | 0.5131 |
| gross_profit_factor | 1.0420 |
| gross_win_rate | 0.5131 |
| sharpe_ratio | -2.7439 |
| sortino_ratio | -0.6441 |
| max_drawdown | 0.5353 |
| cagr | -0.2582 |
| net_avg_win | 53.2213 |
| net_avg_loss | -96.6771 |
| avg_hold_time_bars | 24.9588 |
| exposure | 0.3029 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
