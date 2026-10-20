# EMA Hourly Continuation — DEEP/USDT P8_34

**Symbol:** DEEP/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1057 |
| net_profit_factor | 0.6805 |
| net_win_rate | 0.4740 |
| gross_profit_factor | 0.9664 |
| gross_win_rate | 0.4816 |
| sharpe_ratio | -5.7015 |
| sortino_ratio | -2.9164 |
| max_drawdown | 0.9444 |
| cagr | -0.7541 |
| net_avg_win | 40.0036 |
| net_avg_loss | -52.9689 |
| avg_hold_time_bars | 5.3491 |
| exposure | 0.3201 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
