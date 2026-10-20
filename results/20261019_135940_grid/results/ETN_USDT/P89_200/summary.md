# EMA Hourly Continuation — ETN/USDT P89_200

**Symbol:** ETN/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 440 |
| net_profit_factor | 0.4825 |
| net_win_rate | 0.4068 |
| gross_profit_factor | 0.7175 |
| gross_win_rate | 0.4182 |
| sharpe_ratio | -5.6789 |
| sortino_ratio | -1.8426 |
| max_drawdown | 0.8465 |
| cagr | -0.5844 |
| net_avg_win | 43.8598 |
| net_avg_loss | -62.3420 |
| avg_hold_time_bars | 8.9455 |
| exposure | 0.2138 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
