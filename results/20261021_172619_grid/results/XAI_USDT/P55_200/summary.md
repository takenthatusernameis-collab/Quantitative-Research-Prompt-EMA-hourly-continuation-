# EMA Hourly Continuation — XAI/USDT P55_200

**Symbol:** XAI/USDT  |  **P_fast:** 55  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 297 |
| net_profit_factor | 0.8165 |
| net_win_rate | 0.4949 |
| gross_profit_factor | 0.9782 |
| gross_win_rate | 0.4949 |
| sharpe_ratio | -1.0981 |
| sortino_ratio | -0.2706 |
| max_drawdown | 0.3343 |
| cagr | -0.1184 |
| net_avg_win | 82.0972 |
| net_avg_loss | -98.5425 |
| avg_hold_time_bars | 30.0606 |
| exposure | 0.4058 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
