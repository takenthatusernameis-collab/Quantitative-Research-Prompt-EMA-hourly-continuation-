# EMA Hourly Continuation — JUP/USDT P26_200

**Symbol:** JUP/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 438 |
| net_profit_factor | 0.6211 |
| net_win_rate | 0.4543 |
| gross_profit_factor | 0.8672 |
| gross_win_rate | 0.4566 |
| sharpe_ratio | -3.4142 |
| sortino_ratio | -0.9976 |
| max_drawdown | 0.7185 |
| cagr | -0.3825 |
| net_avg_win | 57.8291 |
| net_avg_loss | -77.5213 |
| avg_hold_time_bars | 27.1895 |
| exposure | 0.5413 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
