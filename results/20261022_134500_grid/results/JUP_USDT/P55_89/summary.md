# EMA Hourly Continuation — JUP/USDT P55_89

**Symbol:** JUP/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 658 |
| net_profit_factor | 0.4053 |
| net_win_rate | 0.4498 |
| gross_profit_factor | 0.7183 |
| gross_win_rate | 0.4559 |
| sharpe_ratio | -5.9989 |
| sortino_ratio | -2.1608 |
| max_drawdown | 0.9353 |
| cagr | -0.6585 |
| net_avg_win | 21.4711 |
| net_avg_loss | -43.3212 |
| avg_hold_time_bars | 3.7128 |
| exposure | 0.1110 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
