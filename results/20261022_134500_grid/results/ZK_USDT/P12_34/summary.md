# EMA Hourly Continuation — ZK/USDT P12_34

**Symbol:** ZK/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1237 |
| net_profit_factor | 0.6021 |
| net_win_rate | 0.4470 |
| gross_profit_factor | 0.9914 |
| gross_win_rate | 0.4568 |
| sharpe_ratio | -8.0386 |
| sortino_ratio | -4.1233 |
| max_drawdown | 0.9912 |
| cagr | -0.8649 |
| net_avg_win | 27.1168 |
| net_avg_loss | -36.4085 |
| avg_hold_time_bars | 4.0582 |
| exposure | 0.2447 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
