# EMA Hourly Continuation — CFX/USDT P8_26

**Symbol:** CFX/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1503 |
| net_profit_factor | 0.4165 |
| net_win_rate | 0.4158 |
| gross_profit_factor | 0.8340 |
| gross_win_rate | 0.4365 |
| sharpe_ratio | -11.2630 |
| sortino_ratio | -6.1886 |
| max_drawdown | 0.9996 |
| cagr | -0.9534 |
| net_avg_win | 11.4158 |
| net_avg_loss | -19.5106 |
| avg_hold_time_bars | 4.2269 |
| exposure | 0.2888 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
