# EMA Hourly Continuation — IOST/USDT P26_55

**Symbol:** IOST/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 505 |
| net_profit_factor | 0.7226 |
| net_win_rate | 0.5149 |
| gross_profit_factor | 1.0657 |
| gross_win_rate | 0.5149 |
| sharpe_ratio | -2.3888 |
| sortino_ratio | -0.7734 |
| max_drawdown | 0.6340 |
| cagr | -0.2979 |
| net_avg_win | 58.9783 |
| net_avg_loss | -86.6169 |
| avg_hold_time_bars | 7.9327 |
| exposure | 0.1821 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
