# EMA Hourly Continuation — SKY/USDT P55_200

**Symbol:** SKY/USDT  |  **P_fast:** 55  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 287 |
| net_profit_factor | 0.8993 |
| net_win_rate | 0.5331 |
| gross_profit_factor | 1.1290 |
| gross_win_rate | 0.5331 |
| sharpe_ratio | -0.5921 |
| sortino_ratio | -0.1602 |
| max_drawdown | 0.3250 |
| cagr | -0.0743 |
| net_avg_win | 85.3958 |
| net_avg_loss | -108.4181 |
| avg_hold_time_bars | 20.0836 |
| exposure | 0.3214 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
