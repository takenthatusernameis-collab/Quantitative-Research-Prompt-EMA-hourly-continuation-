# EMA Hourly Continuation — ETHFI/USDT P89_100

**Symbol:** ETHFI/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 626 |
| net_profit_factor | 0.3247 |
| net_win_rate | 0.4073 |
| gross_profit_factor | 0.7864 |
| gross_win_rate | 0.4297 |
| sharpe_ratio | -8.3728 |
| sortino_ratio | -3.0036 |
| max_drawdown | 0.9790 |
| cagr | -0.7842 |
| net_avg_win | 18.4578 |
| net_avg_loss | -39.0676 |
| avg_hold_time_bars | 1.9393 |
| exposure | 0.0552 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
