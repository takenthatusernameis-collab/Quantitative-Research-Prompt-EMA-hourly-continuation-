# EMA Hourly Continuation — BAT/USDT P8_20

**Symbol:** BAT/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 711 |
| net_profit_factor | 0.6414 |
| net_win_rate | 0.4838 |
| gross_profit_factor | 0.9969 |
| gross_win_rate | 0.4852 |
| sharpe_ratio | -4.1416 |
| sortino_ratio | -1.5846 |
| max_drawdown | 0.8409 |
| cagr | -0.5159 |
| net_avg_win | 43.5835 |
| net_avg_loss | -63.6942 |
| avg_hold_time_bars | 5.3319 |
| exposure | 0.1723 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
