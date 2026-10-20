# EMA Hourly Continuation — FLOW/USDT P34_50

**Symbol:** FLOW/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 928 |
| net_profit_factor | 0.3014 |
| net_win_rate | 0.4041 |
| gross_profit_factor | 0.6908 |
| gross_win_rate | 0.4267 |
| sharpe_ratio | -10.1341 |
| sortino_ratio | -4.4200 |
| max_drawdown | 0.9965 |
| cagr | -0.8939 |
| net_avg_win | 11.4647 |
| net_avg_loss | -25.7929 |
| avg_hold_time_bars | 2.8039 |
| exposure | 0.1183 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
