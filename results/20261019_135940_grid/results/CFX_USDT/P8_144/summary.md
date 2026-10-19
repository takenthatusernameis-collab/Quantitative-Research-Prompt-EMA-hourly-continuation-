# EMA Hourly Continuation — CFX/USDT P8_144

**Symbol:** CFX/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 437 |
| net_profit_factor | 0.7672 |
| net_win_rate | 0.5149 |
| gross_profit_factor | 1.0998 |
| gross_win_rate | 0.5217 |
| sharpe_ratio | -1.8569 |
| sortino_ratio | -0.5498 |
| max_drawdown | 0.5117 |
| cagr | -0.2285 |
| net_avg_win | 70.1172 |
| net_avg_loss | -97.0011 |
| avg_hold_time_bars | 38.1373 |
| exposure | 0.7575 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
