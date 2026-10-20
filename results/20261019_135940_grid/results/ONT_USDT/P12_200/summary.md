# EMA Hourly Continuation — ONT/USDT P12_200

**Symbol:** ONT/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 446 |
| net_profit_factor | 0.5431 |
| net_win_rate | 0.4170 |
| gross_profit_factor | 0.7486 |
| gross_win_rate | 0.4260 |
| sharpe_ratio | -4.0636 |
| sortino_ratio | -1.2018 |
| max_drawdown | 0.7711 |
| cagr | -0.4345 |
| net_avg_win | 48.7278 |
| net_avg_loss | -64.1901 |
| avg_hold_time_bars | 33.8610 |
| exposure | 0.6834 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
