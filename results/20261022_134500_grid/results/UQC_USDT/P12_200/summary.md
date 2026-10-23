# EMA Hourly Continuation — UQC/USDT P12_200

**Symbol:** UQC/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 178 |
| net_profit_factor | 0.3448 |
| net_win_rate | 0.2921 |
| gross_profit_factor | 0.4346 |
| gross_win_rate | 0.2921 |
| sharpe_ratio | -4.4579 |
| sortino_ratio | -0.8282 |
| max_drawdown | 0.6371 |
| cagr | -0.3279 |
| net_avg_win | 64.0657 |
| net_avg_loss | -76.6763 |
| avg_hold_time_bars | 98.3820 |
| exposure | 0.7926 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
