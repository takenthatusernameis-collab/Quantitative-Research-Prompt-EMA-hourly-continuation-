# EMA Hourly Continuation — ALPINE/USDT P26_34

**Symbol:** ALPINE/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 981 |
| net_profit_factor | 0.3230 |
| net_win_rate | 0.3598 |
| gross_profit_factor | 0.7507 |
| gross_win_rate | 0.4128 |
| sharpe_ratio | -12.0083 |
| sortino_ratio | -5.4158 |
| max_drawdown | 0.9991 |
| cagr | -0.9376 |
| net_avg_win | 13.5021 |
| net_avg_loss | -23.4981 |
| avg_hold_time_bars | 3.5821 |
| exposure | 0.1597 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
