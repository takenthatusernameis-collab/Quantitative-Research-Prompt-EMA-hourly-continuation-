# EMA Hourly Continuation — NEAR/USDT P89_200

**Symbol:** NEAR/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 272 |
| net_profit_factor | 0.7794 |
| net_win_rate | 0.4926 |
| gross_profit_factor | 0.9660 |
| gross_win_rate | 0.4926 |
| sharpe_ratio | -1.2492 |
| sortino_ratio | -0.2949 |
| max_drawdown | 0.3347 |
| cagr | -0.1271 |
| net_avg_win | 76.2643 |
| net_avg_loss | -95.0172 |
| avg_hold_time_bars | 15.5588 |
| exposure | 0.1924 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
