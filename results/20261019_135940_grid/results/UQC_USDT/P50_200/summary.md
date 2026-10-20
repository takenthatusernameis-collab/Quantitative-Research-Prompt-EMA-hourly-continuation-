# EMA Hourly Continuation — UQC/USDT P50_200

**Symbol:** UQC/USDT  |  **P_fast:** 50  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 231 |
| net_profit_factor | 0.2508 |
| net_win_rate | 0.2987 |
| gross_profit_factor | 0.4101 |
| gross_win_rate | 0.3030 |
| sharpe_ratio | -5.6035 |
| sortino_ratio | -1.1893 |
| max_drawdown | 0.7835 |
| cagr | -0.4549 |
| net_avg_win | 38.0094 |
| net_avg_loss | -64.5555 |
| avg_hold_time_bars | 55.6017 |
| exposure | 0.5813 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
