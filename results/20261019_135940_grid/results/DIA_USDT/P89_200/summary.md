# EMA Hourly Continuation — DIA/USDT P89_200

**Symbol:** DIA/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 385 |
| net_profit_factor | 0.7631 |
| net_win_rate | 0.5221 |
| gross_profit_factor | 1.1705 |
| gross_win_rate | 0.5351 |
| sharpe_ratio | -1.6997 |
| sortino_ratio | -0.4724 |
| max_drawdown | 0.5108 |
| cagr | -0.1995 |
| net_avg_win | 68.8555 |
| net_avg_loss | -98.5619 |
| avg_hold_time_bars | 12.7584 |
| exposure | 0.2223 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
