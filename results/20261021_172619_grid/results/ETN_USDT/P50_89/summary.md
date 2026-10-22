# EMA Hourly Continuation — ETN/USDT P50_89

**Symbol:** ETN/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 249 |
| net_profit_factor | 0.4437 |
| net_win_rate | 0.3735 |
| gross_profit_factor | 0.5719 |
| gross_win_rate | 0.3735 |
| sharpe_ratio | -4.1051 |
| sortino_ratio | -0.9988 |
| max_drawdown | 0.6328 |
| cagr | -0.3711 |
| net_avg_win | 53.3977 |
| net_avg_loss | -71.7487 |
| avg_hold_time_bars | 7.8996 |
| exposure | 0.1068 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
