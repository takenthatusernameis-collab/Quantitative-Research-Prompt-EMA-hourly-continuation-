# EMA Hourly Continuation — MLK/USDT P34_89

**Symbol:** MLK/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 935 |
| net_profit_factor | 0.2630 |
| net_win_rate | 0.2738 |
| gross_profit_factor | 0.5042 |
| gross_win_rate | 0.2845 |
| sharpe_ratio | -13.4311 |
| sortino_ratio | -5.8944 |
| max_drawdown | 0.9995 |
| cagr | -0.9492 |
| net_avg_win | 13.9355 |
| net_avg_loss | -19.9735 |
| avg_hold_time_bars | 5.8620 |
| exposure | 0.2480 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
