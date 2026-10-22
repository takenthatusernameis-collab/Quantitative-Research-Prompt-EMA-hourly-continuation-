# EMA Hourly Continuation — LUNC/USDT P20_55

**Symbol:** LUNC/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1011 |
| net_profit_factor | 0.3642 |
| net_win_rate | 0.4233 |
| gross_profit_factor | 0.7337 |
| gross_win_rate | 0.4392 |
| sharpe_ratio | -8.9268 |
| sortino_ratio | -4.0055 |
| max_drawdown | 0.9933 |
| cagr | -0.8623 |
| net_avg_win | 13.2888 |
| net_avg_loss | -26.7903 |
| avg_hold_time_bars | 5.1019 |
| exposure | 0.2345 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
