# EMA Hourly Continuation — CTC/USDT P144_200

**Symbol:** CTC/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 427 |
| net_profit_factor | 0.3774 |
| net_win_rate | 0.4052 |
| gross_profit_factor | 0.8230 |
| gross_win_rate | 0.4333 |
| sharpe_ratio | -6.3138 |
| sortino_ratio | -1.8548 |
| max_drawdown | 0.9053 |
| cagr | -0.6062 |
| net_avg_win | 31.6669 |
| net_avg_loss | -57.1461 |
| avg_hold_time_bars | 4.3653 |
| exposure | 0.0847 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
