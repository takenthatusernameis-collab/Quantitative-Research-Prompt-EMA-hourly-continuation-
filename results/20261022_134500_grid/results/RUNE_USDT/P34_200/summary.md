# EMA Hourly Continuation — RUNE/USDT P34_200

**Symbol:** RUNE/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 291 |
| net_profit_factor | 0.7577 |
| net_win_rate | 0.5052 |
| gross_profit_factor | 1.0274 |
| gross_win_rate | 0.5120 |
| sharpe_ratio | -1.3783 |
| sortino_ratio | -0.3337 |
| max_drawdown | 0.3781 |
| cagr | -0.1463 |
| net_avg_win | 69.7400 |
| net_avg_loss | -93.9578 |
| avg_hold_time_bars | 43.7766 |
| exposure | 0.5790 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
