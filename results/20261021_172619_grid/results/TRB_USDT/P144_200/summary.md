# EMA Hourly Continuation — TRB/USDT P144_200

**Symbol:** TRB/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 204 |
| net_profit_factor | 0.6948 |
| net_win_rate | 0.4902 |
| gross_profit_factor | 0.9415 |
| gross_win_rate | 0.4902 |
| sharpe_ratio | -1.5309 |
| sortino_ratio | -0.3126 |
| max_drawdown | 0.3094 |
| cagr | -0.1333 |
| net_avg_win | 68.9504 |
| net_avg_loss | -95.4253 |
| avg_hold_time_bars | 7.2745 |
| exposure | 0.0672 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
