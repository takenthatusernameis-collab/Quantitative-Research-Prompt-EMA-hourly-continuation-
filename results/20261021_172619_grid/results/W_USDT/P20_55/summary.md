# EMA Hourly Continuation — W/USDT P20_55

**Symbol:** W/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 521 |
| net_profit_factor | 0.8269 |
| net_win_rate | 0.5048 |
| gross_profit_factor | 1.0288 |
| gross_win_rate | 0.5067 |
| sharpe_ratio | -1.4415 |
| sortino_ratio | -0.4719 |
| max_drawdown | 0.4630 |
| cagr | -0.1966 |
| net_avg_win | 76.7895 |
| net_avg_loss | -94.6686 |
| avg_hold_time_bars | 8.8023 |
| exposure | 0.2085 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
