# EMA Hourly Continuation — JASMY/USDT P21_50

**Symbol:** JASMY/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 435 |
| net_profit_factor | 0.7865 |
| net_win_rate | 0.5057 |
| gross_profit_factor | 1.0128 |
| gross_win_rate | 0.5057 |
| sharpe_ratio | -1.5415 |
| sortino_ratio | -0.4615 |
| max_drawdown | 0.4454 |
| cagr | -0.1919 |
| net_avg_win | 69.3954 |
| net_avg_loss | -90.2797 |
| avg_hold_time_bars | 6.7034 |
| exposure | 0.1325 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
