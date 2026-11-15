# EMA Hourly Continuation — CERE/USDT P144_200

**Symbol:** CERE/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 490 |
| net_profit_factor | 0.4249 |
| net_win_rate | 0.2980 |
| gross_profit_factor | 0.7137 |
| gross_win_rate | 0.3143 |
| sharpe_ratio | -9.4067 |
| sortino_ratio | -3.0046 |
| max_drawdown | 0.9823 |
| cagr | -0.7960 |
| net_avg_win | 49.6770 |
| net_avg_loss | -49.6169 |
| avg_hold_time_bars | 6.1980 |
| exposure | 0.1380 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
