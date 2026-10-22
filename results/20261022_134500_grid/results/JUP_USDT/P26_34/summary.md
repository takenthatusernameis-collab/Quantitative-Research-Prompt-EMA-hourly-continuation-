# EMA Hourly Continuation — JUP/USDT P26_34

**Symbol:** JUP/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1074 |
| net_profit_factor | 0.3371 |
| net_win_rate | 0.4274 |
| gross_profit_factor | 0.8027 |
| gross_win_rate | 0.4507 |
| sharpe_ratio | -10.3900 |
| sortino_ratio | -4.8480 |
| max_drawdown | 0.9980 |
| cagr | -0.9160 |
| net_avg_win | 11.0545 |
| net_avg_loss | -24.4782 |
| avg_hold_time_bars | 2.1564 |
| exposure | 0.1053 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
