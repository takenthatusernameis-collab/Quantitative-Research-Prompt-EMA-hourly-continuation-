# EMA Hourly Continuation — ENA/USDT P55_200

**Symbol:** ENA/USDT  |  **P_fast:** 55  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 372 |
| net_profit_factor | 0.6665 |
| net_win_rate | 0.4704 |
| gross_profit_factor | 0.8855 |
| gross_win_rate | 0.4731 |
| sharpe_ratio | -2.4858 |
| sortino_ratio | -0.6711 |
| max_drawdown | 0.5736 |
| cagr | -0.2740 |
| net_avg_win | 63.0977 |
| net_avg_loss | -84.1002 |
| avg_hold_time_bars | 18.5618 |
| exposure | 0.3139 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
