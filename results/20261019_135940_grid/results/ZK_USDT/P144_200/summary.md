# EMA Hourly Continuation — ZK/USDT P144_200

**Symbol:** ZK/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 407 |
| net_profit_factor | 0.5117 |
| net_win_rate | 0.4496 |
| gross_profit_factor | 0.8174 |
| gross_win_rate | 0.4570 |
| sharpe_ratio | -4.2411 |
| sortino_ratio | -1.2456 |
| max_drawdown | 0.7646 |
| cagr | -0.4532 |
| net_avg_win | 43.3267 |
| net_avg_loss | -69.1784 |
| avg_hold_time_bars | 5.5528 |
| exposure | 0.1102 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
