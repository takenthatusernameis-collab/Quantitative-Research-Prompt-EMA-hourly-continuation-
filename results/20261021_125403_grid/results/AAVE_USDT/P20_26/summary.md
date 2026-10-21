# EMA Hourly Continuation — AAVE/USDT P20_26

**Symbol:** AAVE/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 136 |
| net_profit_factor | 0.6395 |
| net_win_rate | 0.4632 |
| gross_profit_factor | 0.8826 |
| gross_win_rate | 0.4632 |
| sharpe_ratio | -1.7112 |
| sortino_ratio | -0.2852 |
| max_drawdown | 0.3065 |
| cagr | -0.1229 |
| net_avg_win | 79.0098 |
| net_avg_loss | -106.6324 |
| avg_hold_time_bars | 6.1103 |
| exposure | 0.0378 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
