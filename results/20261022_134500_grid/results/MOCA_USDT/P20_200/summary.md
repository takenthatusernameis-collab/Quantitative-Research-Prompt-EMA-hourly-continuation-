# EMA Hourly Continuation — MOCA/USDT P20_200

**Symbol:** MOCA/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 344 |
| net_profit_factor | 0.5843 |
| net_win_rate | 0.4448 |
| gross_profit_factor | 0.8022 |
| gross_win_rate | 0.4477 |
| sharpe_ratio | -3.3731 |
| sortino_ratio | -0.9220 |
| max_drawdown | 0.6393 |
| cagr | -0.3576 |
| net_avg_win | 58.3232 |
| net_avg_loss | -79.9604 |
| avg_hold_time_bars | 36.8227 |
| exposure | 0.6350 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
