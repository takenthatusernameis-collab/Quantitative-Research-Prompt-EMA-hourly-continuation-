# EMA Hourly Continuation — MNT/USDT P12_200

**Symbol:** MNT/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 234 |
| net_profit_factor | 0.9548 |
| net_win_rate | 0.5342 |
| gross_profit_factor | 1.1461 |
| gross_win_rate | 0.5342 |
| sharpe_ratio | -0.1773 |
| sortino_ratio | -0.0391 |
| max_drawdown | 0.1316 |
| cagr | -0.0216 |
| net_avg_win | 90.2982 |
| net_avg_loss | -108.4502 |
| avg_hold_time_bars | 73.7991 |
| exposure | 0.7850 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
