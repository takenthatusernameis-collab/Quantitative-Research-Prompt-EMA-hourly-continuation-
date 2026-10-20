# EMA Hourly Continuation — CGPT/USDT P144_200

**Symbol:** CGPT/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 399 |
| net_profit_factor | 0.5497 |
| net_win_rate | 0.4812 |
| gross_profit_factor | 0.9836 |
| gross_win_rate | 0.4837 |
| sharpe_ratio | -3.9512 |
| sortino_ratio | -1.1147 |
| max_drawdown | 0.7548 |
| cagr | -0.4194 |
| net_avg_win | 47.3415 |
| net_avg_loss | -79.8877 |
| avg_hold_time_bars | 4.4135 |
| exposure | 0.0800 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
