# EMA Hourly Continuation — ZK/USDT P89_100

**Symbol:** ZK/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 119 |
| net_profit_factor | 0.9013 |
| net_win_rate | 0.5546 |
| gross_profit_factor | 1.2262 |
| gross_win_rate | 0.5546 |
| sharpe_ratio | -0.3143 |
| sortino_ratio | -0.0515 |
| max_drawdown | 0.1094 |
| cagr | -0.0248 |
| net_avg_win | 79.0811 |
| net_avg_loss | -109.2680 |
| avg_hold_time_bars | 8.0504 |
| exposure | 0.0467 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
