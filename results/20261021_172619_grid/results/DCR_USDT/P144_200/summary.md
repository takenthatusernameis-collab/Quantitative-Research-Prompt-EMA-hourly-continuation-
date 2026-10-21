# EMA Hourly Continuation — DCR/USDT P144_200

**Symbol:** DCR/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 221 |
| net_profit_factor | 0.5198 |
| net_win_rate | 0.4434 |
| gross_profit_factor | 0.7937 |
| gross_win_rate | 0.4434 |
| sharpe_ratio | -2.8879 |
| sortino_ratio | -0.6116 |
| max_drawdown | 0.5186 |
| cagr | -0.2446 |
| net_avg_win | 56.0140 |
| net_avg_loss | -85.8631 |
| avg_hold_time_bars | 6.7421 |
| exposure | 0.0674 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
