# EMA Hourly Continuation — CYBER/USDT P50_55

**Symbol:** CYBER/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 184 |
| net_profit_factor | 0.7160 |
| net_win_rate | 0.5272 |
| gross_profit_factor | 1.1113 |
| gross_win_rate | 0.5272 |
| sharpe_ratio | -1.4594 |
| sortino_ratio | -0.2846 |
| max_drawdown | 0.3338 |
| cagr | -0.1230 |
| net_avg_win | 73.0156 |
| net_avg_loss | -113.6940 |
| avg_hold_time_bars | 6.5543 |
| exposure | 0.0548 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
