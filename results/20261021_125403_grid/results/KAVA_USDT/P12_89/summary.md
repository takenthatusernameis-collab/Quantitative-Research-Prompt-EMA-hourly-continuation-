# EMA Hourly Continuation — KAVA/USDT P12_89

**Symbol:** KAVA/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 550 |
| net_profit_factor | 0.7323 |
| net_win_rate | 0.4836 |
| gross_profit_factor | 0.9949 |
| gross_win_rate | 0.4873 |
| sharpe_ratio | -2.8683 |
| sortino_ratio | -0.9574 |
| max_drawdown | 0.7015 |
| cagr | -0.3602 |
| net_avg_win | 69.3356 |
| net_avg_loss | -88.6809 |
| avg_hold_time_bars | 22.1109 |
| exposure | 0.5528 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
