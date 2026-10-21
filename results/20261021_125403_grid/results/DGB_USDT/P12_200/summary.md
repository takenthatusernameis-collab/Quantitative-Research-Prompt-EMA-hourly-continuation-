# EMA Hourly Continuation — DGB/USDT P12_200

**Symbol:** DGB/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 367 |
| net_profit_factor | 0.7695 |
| net_win_rate | 0.4768 |
| gross_profit_factor | 0.9137 |
| gross_win_rate | 0.4768 |
| sharpe_ratio | -1.6342 |
| sortino_ratio | -0.4451 |
| max_drawdown | 0.4492 |
| cagr | -0.1863 |
| net_avg_win | 77.1195 |
| net_avg_loss | -91.3438 |
| avg_hold_time_bars | 42.1008 |
| exposure | 0.7023 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
