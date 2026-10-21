# EMA Hourly Continuation — WOO/USDT P21_144

**Symbol:** WOO/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 382 |
| net_profit_factor | 0.8098 |
| net_win_rate | 0.4869 |
| gross_profit_factor | 0.9735 |
| gross_win_rate | 0.4895 |
| sharpe_ratio | -1.4662 |
| sortino_ratio | -0.4086 |
| max_drawdown | 0.4838 |
| cagr | -0.1726 |
| net_avg_win | 86.6873 |
| net_avg_loss | -101.5803 |
| avg_hold_time_bars | 31.4503 |
| exposure | 0.5461 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
