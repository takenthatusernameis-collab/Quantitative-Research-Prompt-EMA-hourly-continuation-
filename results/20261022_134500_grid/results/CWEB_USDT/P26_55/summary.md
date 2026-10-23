# EMA Hourly Continuation — CWEB/USDT P26_55

**Symbol:** CWEB/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 827 |
| net_profit_factor | 0.3449 |
| net_win_rate | 0.3144 |
| gross_profit_factor | 0.7065 |
| gross_win_rate | 0.3313 |
| sharpe_ratio | -12.6521 |
| sortino_ratio | -5.2506 |
| max_drawdown | 0.9993 |
| cagr | -0.9448 |
| net_avg_win | 20.2325 |
| net_avg_loss | -26.9022 |
| avg_hold_time_bars | 5.8089 |
| exposure | 0.2184 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
