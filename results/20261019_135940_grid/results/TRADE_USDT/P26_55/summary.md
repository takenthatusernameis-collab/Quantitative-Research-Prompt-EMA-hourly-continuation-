# EMA Hourly Continuation — TRADE/USDT P26_55

**Symbol:** TRADE/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 741 |
| net_profit_factor | 0.4931 |
| net_win_rate | 0.4143 |
| gross_profit_factor | 0.8342 |
| gross_win_rate | 0.4197 |
| sharpe_ratio | -7.1961 |
| sortino_ratio | -2.7249 |
| max_drawdown | 0.9711 |
| cagr | -0.7534 |
| net_avg_win | 30.7409 |
| net_avg_loss | -44.1022 |
| avg_hold_time_bars | 5.6167 |
| exposure | 0.1892 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
