# EMA Hourly Continuation — ATOM/USDT P8_55

**Symbol:** ATOM/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 905 |
| net_profit_factor | 0.5057 |
| net_win_rate | 0.4619 |
| gross_profit_factor | 0.9227 |
| gross_win_rate | 0.4762 |
| sharpe_ratio | -6.1148 |
| sortino_ratio | -2.5743 |
| max_drawdown | 0.9596 |
| cagr | -0.7183 |
| net_avg_win | 23.4565 |
| net_avg_loss | -39.8143 |
| avg_hold_time_bars | 13.1878 |
| exposure | 0.5425 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
