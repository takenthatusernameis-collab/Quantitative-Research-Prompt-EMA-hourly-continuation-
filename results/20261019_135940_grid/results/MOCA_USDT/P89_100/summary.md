# EMA Hourly Continuation — MOCA/USDT P89_100

**Symbol:** MOCA/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 514 |
| net_profit_factor | 0.3018 |
| net_win_rate | 0.3716 |
| gross_profit_factor | 0.7394 |
| gross_win_rate | 0.4222 |
| sharpe_ratio | -9.2447 |
| sortino_ratio | -3.1556 |
| max_drawdown | 0.9804 |
| cagr | -0.8204 |
| net_avg_win | 22.1732 |
| net_avg_loss | -43.4505 |
| avg_hold_time_bars | 2.4397 |
| exposure | 0.0629 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
