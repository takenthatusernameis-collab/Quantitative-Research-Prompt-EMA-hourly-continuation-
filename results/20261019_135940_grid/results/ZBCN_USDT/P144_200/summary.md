# EMA Hourly Continuation — ZBCN/USDT P144_200

**Symbol:** ZBCN/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 479 |
| net_profit_factor | 0.5141 |
| net_win_rate | 0.4739 |
| gross_profit_factor | 0.8444 |
| gross_win_rate | 0.4760 |
| sharpe_ratio | -4.0741 |
| sortino_ratio | -1.2739 |
| max_drawdown | 0.7947 |
| cagr | -0.4576 |
| net_avg_win | 36.3022 |
| net_avg_loss | -63.6095 |
| avg_hold_time_bars | 3.2985 |
| exposure | 0.0731 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
