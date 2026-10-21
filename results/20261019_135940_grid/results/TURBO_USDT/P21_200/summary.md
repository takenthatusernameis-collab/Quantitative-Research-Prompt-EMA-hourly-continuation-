# EMA Hourly Continuation — TURBO/USDT P21_200

**Symbol:** TURBO/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 333 |
| net_profit_factor | 0.6336 |
| net_win_rate | 0.4535 |
| gross_profit_factor | 0.8516 |
| gross_win_rate | 0.4565 |
| sharpe_ratio | -3.1094 |
| sortino_ratio | -0.8720 |
| max_drawdown | 0.5938 |
| cagr | -0.3374 |
| net_avg_win | 66.1248 |
| net_avg_loss | -86.5864 |
| avg_hold_time_bars | 34.2943 |
| exposure | 0.6230 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
