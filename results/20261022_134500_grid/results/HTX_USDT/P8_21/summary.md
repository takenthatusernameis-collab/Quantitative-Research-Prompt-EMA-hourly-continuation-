# EMA Hourly Continuation — HTX/USDT P8_21

**Symbol:** HTX/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1765 |
| net_profit_factor | 0.1128 |
| net_win_rate | 0.2351 |
| gross_profit_factor | 0.4386 |
| gross_win_rate | 0.3241 |
| sharpe_ratio | -23.9220 |
| sortino_ratio | -15.5242 |
| max_drawdown | 1.0000 |
| cagr | -0.9998 |
| net_avg_win | 3.0622 |
| net_avg_loss | -8.3488 |
| avg_hold_time_bars | 3.3445 |
| exposure | 0.2671 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
