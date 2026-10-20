# EMA Hourly Continuation — WAVES/USDT P8_50

**Symbol:** WAVES/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1300 |
| net_profit_factor | 0.4945 |
| net_win_rate | 0.4285 |
| gross_profit_factor | 0.9389 |
| gross_win_rate | 0.4623 |
| sharpe_ratio | -9.2413 |
| sortino_ratio | -4.6826 |
| max_drawdown | 0.9971 |
| cagr | -0.9017 |
| net_avg_win | 17.5138 |
| net_avg_loss | -26.5488 |
| avg_hold_time_bars | 7.5346 |
| exposure | 0.4452 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
