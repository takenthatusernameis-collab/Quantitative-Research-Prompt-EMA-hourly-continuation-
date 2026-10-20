# EMA Hourly Continuation — RLC/USDT P21_144

**Symbol:** RLC/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 579 |
| net_profit_factor | 0.6574 |
| net_win_rate | 0.4819 |
| gross_profit_factor | 0.9406 |
| gross_win_rate | 0.4905 |
| sharpe_ratio | -3.1976 |
| sortino_ratio | -1.0880 |
| max_drawdown | 0.7512 |
| cagr | -0.4020 |
| net_avg_win | 49.8658 |
| net_avg_loss | -70.5435 |
| avg_hold_time_bars | 18.7772 |
| exposure | 0.4942 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
