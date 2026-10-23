# EMA Hourly Continuation — MOVR/USDT P26_55

**Symbol:** MOVR/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 938 |
| net_profit_factor | 0.4687 |
| net_win_rate | 0.4531 |
| gross_profit_factor | 0.9102 |
| gross_win_rate | 0.4670 |
| sharpe_ratio | -7.0597 |
| sortino_ratio | -3.0311 |
| max_drawdown | 0.9784 |
| cagr | -0.7779 |
| net_avg_win | 20.2820 |
| net_avg_loss | -35.8506 |
| avg_hold_time_bars | 4.1066 |
| exposure | 0.1751 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
