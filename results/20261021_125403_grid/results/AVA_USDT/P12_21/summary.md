# EMA Hourly Continuation — AVA/USDT P12_21

**Symbol:** AVA/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 351 |
| net_profit_factor | 0.6928 |
| net_win_rate | 0.5157 |
| gross_profit_factor | 1.0344 |
| gross_win_rate | 0.5157 |
| sharpe_ratio | -1.9948 |
| sortino_ratio | -0.5394 |
| max_drawdown | 0.4846 |
| cagr | -0.2176 |
| net_avg_win | 57.3224 |
| net_avg_loss | -88.0913 |
| avg_hold_time_bars | 4.7009 |
| exposure | 0.0750 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
