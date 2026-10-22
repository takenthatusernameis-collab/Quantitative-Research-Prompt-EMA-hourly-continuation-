# EMA Hourly Continuation — MLK/USDT P34_55

**Symbol:** MLK/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 288 |
| net_profit_factor | 0.3308 |
| net_win_rate | 0.3333 |
| gross_profit_factor | 0.5367 |
| gross_win_rate | 0.3403 |
| sharpe_ratio | -5.6157 |
| sortino_ratio | -1.3598 |
| max_drawdown | 0.8058 |
| cagr | -0.4711 |
| net_avg_win | 41.1688 |
| net_avg_loss | -62.2207 |
| avg_hold_time_bars | 6.6458 |
| exposure | 0.0866 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
