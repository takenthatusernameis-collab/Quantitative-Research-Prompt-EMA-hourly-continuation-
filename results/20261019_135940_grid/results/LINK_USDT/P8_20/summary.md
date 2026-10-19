# EMA Hourly Continuation — LINK/USDT P8_20

**Symbol:** LINK/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1618 |
| net_profit_factor | 0.3553 |
| net_win_rate | 0.4425 |
| gross_profit_factor | 0.9189 |
| gross_win_rate | 0.4728 |
| sharpe_ratio | -12.2087 |
| sortino_ratio | -6.9096 |
| max_drawdown | 0.9999 |
| cagr | -0.9727 |
| net_avg_win | 7.6977 |
| net_avg_loss | -17.1955 |
| avg_hold_time_bars | 2.7967 |
| exposure | 0.2057 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
