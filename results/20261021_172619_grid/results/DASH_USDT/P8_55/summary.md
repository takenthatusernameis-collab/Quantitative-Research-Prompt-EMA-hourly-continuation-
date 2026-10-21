# EMA Hourly Continuation — DASH/USDT P8_55

**Symbol:** DASH/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 661 |
| net_profit_factor | 0.7703 |
| net_win_rate | 0.5023 |
| gross_profit_factor | 1.0090 |
| gross_win_rate | 0.5023 |
| sharpe_ratio | -2.0066 |
| sortino_ratio | -0.7395 |
| max_drawdown | 0.5805 |
| cagr | -0.2889 |
| net_avg_win | 58.1114 |
| net_avg_loss | -76.1236 |
| avg_hold_time_bars | 14.9047 |
| exposure | 0.4478 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
