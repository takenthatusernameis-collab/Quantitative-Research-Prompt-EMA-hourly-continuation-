# EMA Hourly Continuation — NEAR/USDT P12_50

**Symbol:** NEAR/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1082 |
| net_profit_factor | 0.5526 |
| net_win_rate | 0.4501 |
| gross_profit_factor | 0.8879 |
| gross_win_rate | 0.4566 |
| sharpe_ratio | -6.7258 |
| sortino_ratio | -3.1014 |
| max_drawdown | 0.9778 |
| cagr | -0.7794 |
| net_avg_win | 24.7955 |
| net_avg_loss | -36.7239 |
| avg_hold_time_bars | 7.1044 |
| exposure | 0.3494 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
