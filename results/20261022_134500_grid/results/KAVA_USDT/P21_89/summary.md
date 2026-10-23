# EMA Hourly Continuation — KAVA/USDT P21_89

**Symbol:** KAVA/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 735 |
| net_profit_factor | 0.5123 |
| net_win_rate | 0.4395 |
| gross_profit_factor | 0.9069 |
| gross_win_rate | 0.4599 |
| sharpe_ratio | -6.3462 |
| sortino_ratio | -2.4104 |
| max_drawdown | 0.9534 |
| cagr | -0.6981 |
| net_avg_win | 30.9186 |
| net_avg_loss | -47.3127 |
| avg_hold_time_bars | 12.2735 |
| exposure | 0.4100 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
