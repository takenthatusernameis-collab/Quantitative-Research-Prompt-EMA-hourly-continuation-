# EMA Hourly Continuation — CWEB/USDT P12_50

**Symbol:** CWEB/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 881 |
| net_profit_factor | 0.4434 |
| net_win_rate | 0.3666 |
| gross_profit_factor | 0.7960 |
| gross_win_rate | 0.3791 |
| sharpe_ratio | -10.5580 |
| sortino_ratio | -4.4120 |
| max_drawdown | 0.9975 |
| cagr | -0.9071 |
| net_avg_win | 24.5979 |
| net_avg_loss | -32.1138 |
| avg_hold_time_bars | 10.7719 |
| exposure | 0.4314 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
