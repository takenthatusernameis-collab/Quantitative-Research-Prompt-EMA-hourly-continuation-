# EMA Hourly Continuation — GALA/USDT P21_89

**Symbol:** GALA/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 460 |
| net_profit_factor | 0.7533 |
| net_win_rate | 0.4826 |
| gross_profit_factor | 0.9208 |
| gross_win_rate | 0.4826 |
| sharpe_ratio | -1.8033 |
| sortino_ratio | -0.5519 |
| max_drawdown | 0.5142 |
| cagr | -0.2242 |
| net_avg_win | 64.8406 |
| net_avg_loss | -80.2867 |
| avg_hold_time_bars | 17.8326 |
| exposure | 0.3729 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
