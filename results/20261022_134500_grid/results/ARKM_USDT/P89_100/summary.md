# EMA Hourly Continuation — ARKM/USDT P89_100

**Symbol:** ARKM/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 661 |
| net_profit_factor | 0.2961 |
| net_win_rate | 0.3949 |
| gross_profit_factor | 0.6731 |
| gross_win_rate | 0.4297 |
| sharpe_ratio | -9.1096 |
| sortino_ratio | -3.3742 |
| max_drawdown | 0.9872 |
| cagr | -0.8228 |
| net_avg_win | 15.9111 |
| net_avg_loss | -35.0581 |
| avg_hold_time_bars | 2.1346 |
| exposure | 0.0641 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
