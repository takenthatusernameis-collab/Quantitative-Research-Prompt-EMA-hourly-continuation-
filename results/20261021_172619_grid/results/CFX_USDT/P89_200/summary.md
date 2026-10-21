# EMA Hourly Continuation — CFX/USDT P89_200

**Symbol:** CFX/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 245 |
| net_profit_factor | 0.8192 |
| net_win_rate | 0.5061 |
| gross_profit_factor | 1.0166 |
| gross_win_rate | 0.5061 |
| sharpe_ratio | -0.9463 |
| sortino_ratio | -0.2125 |
| max_drawdown | 0.2407 |
| cagr | -0.0941 |
| net_avg_win | 80.3092 |
| net_avg_loss | -100.4704 |
| avg_hold_time_bars | 19.6857 |
| exposure | 0.2192 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
