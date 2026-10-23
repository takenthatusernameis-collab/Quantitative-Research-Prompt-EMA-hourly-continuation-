# EMA Hourly Continuation — DODO/USDT P8_89

**Symbol:** DODO/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 812 |
| net_profit_factor | 0.5986 |
| net_win_rate | 0.4421 |
| gross_profit_factor | 0.8897 |
| gross_win_rate | 0.4606 |
| sharpe_ratio | -5.1721 |
| sortino_ratio | -2.0661 |
| max_drawdown | 0.9227 |
| cagr | -0.6267 |
| net_avg_win | 38.0765 |
| net_avg_loss | -50.4122 |
| avg_hold_time_bars | 16.6995 |
| exposure | 0.6136 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
