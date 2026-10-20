# EMA Hourly Continuation — SUSHI/USDT P20_50

**Symbol:** SUSHI/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1008 |
| net_profit_factor | 0.5105 |
| net_win_rate | 0.4315 |
| gross_profit_factor | 0.8811 |
| gross_win_rate | 0.4484 |
| sharpe_ratio | -7.6917 |
| sortino_ratio | -3.4246 |
| max_drawdown | 0.9857 |
| cagr | -0.8138 |
| net_avg_win | 23.6316 |
| net_avg_loss | -35.1408 |
| avg_hold_time_bars | 4.7927 |
| exposure | 0.2186 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
