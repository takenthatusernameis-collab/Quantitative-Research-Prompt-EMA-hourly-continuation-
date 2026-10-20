# EMA Hourly Continuation — MLK/USDT P12_100

**Symbol:** MLK/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 982 |
| net_profit_factor | 0.3710 |
| net_win_rate | 0.3238 |
| gross_profit_factor | 0.6106 |
| gross_win_rate | 0.3279 |
| sharpe_ratio | -11.3950 |
| sortino_ratio | -5.0341 |
| max_drawdown | 0.9984 |
| cagr | -0.9215 |
| net_avg_win | 18.5189 |
| net_avg_loss | -23.9046 |
| avg_hold_time_bars | 11.5132 |
| exposure | 0.5117 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
