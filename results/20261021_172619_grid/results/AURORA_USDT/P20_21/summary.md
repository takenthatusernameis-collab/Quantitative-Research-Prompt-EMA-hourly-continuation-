# EMA Hourly Continuation — AURORA/USDT P20_21

**Symbol:** AURORA/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 171 |
| net_profit_factor | 0.3966 |
| net_win_rate | 0.4035 |
| gross_profit_factor | 0.7195 |
| gross_win_rate | 0.4094 |
| sharpe_ratio | -3.7842 |
| sortino_ratio | -0.7145 |
| max_drawdown | 0.5886 |
| cagr | -0.2881 |
| net_avg_win | 54.6781 |
| net_avg_loss | -93.2601 |
| avg_hold_time_bars | 7.8830 |
| exposure | 0.0613 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
