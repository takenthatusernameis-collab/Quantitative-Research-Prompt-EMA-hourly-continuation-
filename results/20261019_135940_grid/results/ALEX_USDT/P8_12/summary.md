# EMA Hourly Continuation — ALEX/USDT P8_12

**Symbol:** ALEX/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1546 |
| net_profit_factor | 0.2792 |
| net_win_rate | 0.2962 |
| gross_profit_factor | 0.8878 |
| gross_win_rate | 0.3402 |
| sharpe_ratio | -18.2020 |
| sortino_ratio | -10.3140 |
| max_drawdown | 1.0000 |
| cagr | -0.9965 |
| net_avg_win | 8.4591 |
| net_avg_loss | -12.7521 |
| avg_hold_time_bars | 3.0330 |
| exposure | 0.2131 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
