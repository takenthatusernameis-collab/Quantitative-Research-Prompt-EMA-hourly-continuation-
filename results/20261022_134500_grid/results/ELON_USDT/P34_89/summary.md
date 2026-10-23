# EMA Hourly Continuation — ELON/USDT P34_89

**Symbol:** ELON/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 670 |
| net_profit_factor | 0.4036 |
| net_win_rate | 0.4269 |
| gross_profit_factor | 0.7032 |
| gross_win_rate | 0.4358 |
| sharpe_ratio | -6.4026 |
| sortino_ratio | -2.3444 |
| max_drawdown | 0.9452 |
| cagr | -0.6803 |
| net_avg_win | 22.3076 |
| net_avg_loss | -41.1700 |
| avg_hold_time_bars | 7.0493 |
| exposure | 0.2147 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
