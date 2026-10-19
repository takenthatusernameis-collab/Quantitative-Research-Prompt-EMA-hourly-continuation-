# EMA Hourly Continuation — AVAX/USDT P20_50

**Symbol:** AVAX/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 951 |
| net_profit_factor | 0.4975 |
| net_win_rate | 0.4343 |
| gross_profit_factor | 0.9131 |
| gross_win_rate | 0.4479 |
| sharpe_ratio | -8.3427 |
| sortino_ratio | -3.6188 |
| max_drawdown | 0.9901 |
| cagr | -0.8378 |
| net_avg_win | 23.7263 |
| net_avg_loss | -36.6083 |
| avg_hold_time_bars | 4.5773 |
| exposure | 0.1979 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
