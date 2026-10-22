# EMA Hourly Continuation — SUPER/USDT P12_34

**Symbol:** SUPER/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1254 |
| net_profit_factor | 0.4989 |
| net_win_rate | 0.4498 |
| gross_profit_factor | 0.9058 |
| gross_win_rate | 0.4697 |
| sharpe_ratio | -8.0005 |
| sortino_ratio | -3.9789 |
| max_drawdown | 0.9930 |
| cagr | -0.8590 |
| net_avg_win | 17.5224 |
| net_avg_loss | -28.7097 |
| avg_hold_time_bars | 4.3748 |
| exposure | 0.2494 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
