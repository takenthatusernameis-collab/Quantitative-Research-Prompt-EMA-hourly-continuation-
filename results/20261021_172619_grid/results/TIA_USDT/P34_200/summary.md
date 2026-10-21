# EMA Hourly Continuation — TIA/USDT P34_200

**Symbol:** TIA/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 259 |
| net_profit_factor | 0.8687 |
| net_win_rate | 0.5019 |
| gross_profit_factor | 1.0031 |
| gross_win_rate | 0.5019 |
| sharpe_ratio | -0.6937 |
| sortino_ratio | -0.1599 |
| max_drawdown | 0.2302 |
| cagr | -0.0729 |
| net_avg_win | 88.1584 |
| net_avg_loss | -102.2667 |
| avg_hold_time_bars | 45.1969 |
| exposure | 0.5321 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
