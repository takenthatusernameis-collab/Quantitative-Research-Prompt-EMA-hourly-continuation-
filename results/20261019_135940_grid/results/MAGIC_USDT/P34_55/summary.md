# EMA Hourly Continuation — MAGIC/USDT P34_55

**Symbol:** MAGIC/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 865 |
| net_profit_factor | 0.5624 |
| net_win_rate | 0.4705 |
| gross_profit_factor | 1.0120 |
| gross_win_rate | 0.4867 |
| sharpe_ratio | -6.4259 |
| sortino_ratio | -2.6773 |
| max_drawdown | 0.9628 |
| cagr | -0.7264 |
| net_avg_win | 30.3529 |
| net_avg_loss | -47.9643 |
| avg_hold_time_bars | 3.8243 |
| exposure | 0.1504 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
