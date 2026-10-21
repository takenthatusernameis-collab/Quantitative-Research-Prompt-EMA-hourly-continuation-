# EMA Hourly Continuation — XEC/USDT P20_144

**Symbol:** XEC/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 432 |
| net_profit_factor | 0.8037 |
| net_win_rate | 0.5046 |
| gross_profit_factor | 1.0240 |
| gross_win_rate | 0.5046 |
| sharpe_ratio | -1.4765 |
| sortino_ratio | -0.4388 |
| max_drawdown | 0.4814 |
| cagr | -0.1839 |
| net_avg_win | 75.3154 |
| net_avg_loss | -95.4613 |
| avg_hold_time_bars | 27.8958 |
| exposure | 0.5453 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
