# EMA Hourly Continuation — ZEN/USDT P8_26

**Symbol:** ZEN/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 716 |
| net_profit_factor | 0.7408 |
| net_win_rate | 0.5000 |
| gross_profit_factor | 1.0130 |
| gross_win_rate | 0.5000 |
| sharpe_ratio | -2.6519 |
| sortino_ratio | -1.0174 |
| max_drawdown | 0.6906 |
| cagr | -0.3732 |
| net_avg_win | 55.1263 |
| net_avg_loss | -74.4158 |
| avg_hold_time_bars | 6.2570 |
| exposure | 0.2036 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
