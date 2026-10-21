# EMA Hourly Continuation — ENS/USDT P21_200

**Symbol:** ENS/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 247 |
| net_profit_factor | 0.9250 |
| net_win_rate | 0.5263 |
| gross_profit_factor | 1.1051 |
| gross_win_rate | 0.5304 |
| sharpe_ratio | -0.3188 |
| sortino_ratio | -0.0722 |
| max_drawdown | 0.1671 |
| cagr | -0.0358 |
| net_avg_win | 83.1244 |
| net_avg_loss | -99.8455 |
| avg_hold_time_bars | 58.5061 |
| exposure | 0.6569 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
