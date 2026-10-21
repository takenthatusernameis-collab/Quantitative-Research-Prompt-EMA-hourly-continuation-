# EMA Hourly Continuation — ARKM/USDT P20_34

**Symbol:** ARKM/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 340 |
| net_profit_factor | 0.7173 |
| net_win_rate | 0.4824 |
| gross_profit_factor | 0.9496 |
| gross_win_rate | 0.4824 |
| sharpe_ratio | -2.1025 |
| sortino_ratio | -0.5546 |
| max_drawdown | 0.5374 |
| cagr | -0.2245 |
| net_avg_win | 73.0251 |
| net_avg_loss | -94.8623 |
| avg_hold_time_bars | 5.7500 |
| exposure | 0.0889 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
