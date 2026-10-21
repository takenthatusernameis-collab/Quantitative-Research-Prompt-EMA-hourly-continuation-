# EMA Hourly Continuation — WLD/USDT P21_100

**Symbol:** WLD/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 435 |
| net_profit_factor | 0.9943 |
| net_win_rate | 0.5425 |
| gross_profit_factor | 1.1739 |
| gross_win_rate | 0.5425 |
| sharpe_ratio | 0.0269 |
| sortino_ratio | 0.0081 |
| max_drawdown | 0.2863 |
| cagr | -0.0051 |
| net_avg_win | 95.3644 |
| net_avg_loss | -113.7386 |
| avg_hold_time_bars | 20.2207 |
| exposure | 0.3998 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
