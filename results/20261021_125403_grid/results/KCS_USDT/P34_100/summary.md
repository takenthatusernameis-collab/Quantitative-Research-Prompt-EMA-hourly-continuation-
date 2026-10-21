# EMA Hourly Continuation — KCS/USDT P34_100

**Symbol:** KCS/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 381 |
| net_profit_factor | 0.4600 |
| net_win_rate | 0.4436 |
| gross_profit_factor | 0.8093 |
| gross_win_rate | 0.4436 |
| sharpe_ratio | -4.5883 |
| sortino_ratio | -1.2887 |
| max_drawdown | 0.7804 |
| cagr | -0.4486 |
| net_avg_win | 39.0970 |
| net_avg_loss | -67.7570 |
| avg_hold_time_bars | 15.6535 |
| exposure | 0.2711 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
