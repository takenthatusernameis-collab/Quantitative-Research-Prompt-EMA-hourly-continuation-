# EMA Hourly Continuation — BIGTIME/USDT P34_200

**Symbol:** BIGTIME/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 331 |
| net_profit_factor | 0.9130 |
| net_win_rate | 0.5408 |
| gross_profit_factor | 1.1779 |
| gross_win_rate | 0.5408 |
| sharpe_ratio | -0.4939 |
| sortino_ratio | -0.1288 |
| max_drawdown | 0.2808 |
| cagr | -0.0615 |
| net_avg_win | 86.6951 |
| net_avg_loss | -111.8210 |
| avg_hold_time_bars | 37.3082 |
| exposure | 0.5588 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
