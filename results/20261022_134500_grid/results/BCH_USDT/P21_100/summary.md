# EMA Hourly Continuation — BCH/USDT P21_100

**Symbol:** BCH/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 663 |
| net_profit_factor | 0.5331 |
| net_win_rate | 0.4540 |
| gross_profit_factor | 0.9086 |
| gross_win_rate | 0.4691 |
| sharpe_ratio | -5.5425 |
| sortino_ratio | -2.0141 |
| max_drawdown | 0.9201 |
| cagr | -0.6207 |
| net_avg_win | 34.6033 |
| net_avg_loss | -53.9753 |
| avg_hold_time_bars | 13.3741 |
| exposure | 0.4030 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
