# EMA Hourly Continuation — WLD/USDT P12_200

**Symbol:** WLD/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 315 |
| net_profit_factor | 0.8235 |
| net_win_rate | 0.5048 |
| gross_profit_factor | 1.0115 |
| gross_win_rate | 0.5048 |
| sharpe_ratio | -1.0573 |
| sortino_ratio | -0.2636 |
| max_drawdown | 0.3441 |
| cagr | -0.1207 |
| net_avg_win | 80.9793 |
| net_avg_loss | -100.2324 |
| avg_hold_time_bars | 53.3365 |
| exposure | 0.7637 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
