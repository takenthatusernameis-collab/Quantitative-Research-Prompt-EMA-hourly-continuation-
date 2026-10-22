# EMA Hourly Continuation — NEAR/USDT P8_34

**Symbol:** NEAR/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1427 |
| net_profit_factor | 0.5619 |
| net_win_rate | 0.4744 |
| gross_profit_factor | 0.9385 |
| gross_win_rate | 0.4786 |
| sharpe_ratio | -7.2191 |
| sortino_ratio | -3.8283 |
| max_drawdown | 0.9908 |
| cagr | -0.8444 |
| net_avg_win | 18.7688 |
| net_avg_loss | -30.1507 |
| avg_hold_time_bars | 4.9790 |
| exposure | 0.3230 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
