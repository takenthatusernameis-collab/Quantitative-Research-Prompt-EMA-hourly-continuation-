# EMA Hourly Continuation — XRP/USDT P8_34

**Symbol:** XRP/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1469 |
| net_profit_factor | 0.3327 |
| net_win_rate | 0.4275 |
| gross_profit_factor | 0.9521 |
| gross_win_rate | 0.4677 |
| sharpe_ratio | -11.9187 |
| sortino_ratio | -6.4110 |
| max_drawdown | 0.9998 |
| cagr | -0.9663 |
| net_avg_win | 7.9378 |
| net_avg_loss | -17.8156 |
| avg_hold_time_bars | 4.5439 |
| exposure | 0.3034 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
