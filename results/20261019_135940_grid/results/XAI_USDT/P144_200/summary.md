# EMA Hourly Continuation — XAI/USDT P144_200

**Symbol:** XAI/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 403 |
| net_profit_factor | 0.5330 |
| net_win_rate | 0.4690 |
| gross_profit_factor | 0.8908 |
| gross_win_rate | 0.4764 |
| sharpe_ratio | -4.0245 |
| sortino_ratio | -1.1309 |
| max_drawdown | 0.7537 |
| cagr | -0.4276 |
| net_avg_win | 45.5096 |
| net_avg_loss | -75.4124 |
| avg_hold_time_bars | 4.5806 |
| exposure | 0.0839 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
