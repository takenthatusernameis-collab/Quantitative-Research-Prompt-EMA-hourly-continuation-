# EMA Hourly Continuation — LTC/USDT P8_55

**Symbol:** LTC/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 643 |
| net_profit_factor | 0.7008 |
| net_win_rate | 0.4946 |
| gross_profit_factor | 0.9745 |
| gross_win_rate | 0.4946 |
| sharpe_ratio | -2.8365 |
| sortino_ratio | -1.0312 |
| max_drawdown | 0.6975 |
| cagr | -0.3763 |
| net_avg_win | 51.1491 |
| net_avg_loss | -71.4148 |
| avg_hold_time_bars | 14.2131 |
| exposure | 0.4154 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
