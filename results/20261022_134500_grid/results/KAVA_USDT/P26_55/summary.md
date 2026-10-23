# EMA Hourly Continuation — KAVA/USDT P26_55

**Symbol:** KAVA/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 996 |
| net_profit_factor | 0.4639 |
| net_win_rate | 0.4187 |
| gross_profit_factor | 0.9150 |
| gross_win_rate | 0.4588 |
| sharpe_ratio | -9.4952 |
| sortino_ratio | -4.2584 |
| max_drawdown | 0.9955 |
| cagr | -0.8831 |
| net_avg_win | 20.6565 |
| net_avg_loss | -32.0694 |
| avg_hold_time_bars | 4.4839 |
| exposure | 0.2030 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
