# EMA Hourly Continuation — DOGE/USDT P8_55

**Symbol:** DOGE/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1117 |
| net_profit_factor | 0.4949 |
| net_win_rate | 0.4521 |
| gross_profit_factor | 0.8640 |
| gross_win_rate | 0.4673 |
| sharpe_ratio | -7.6405 |
| sortino_ratio | -3.5751 |
| max_drawdown | 0.9885 |
| cagr | -0.8301 |
| net_avg_win | 19.1770 |
| net_avg_loss | -31.9735 |
| avg_hold_time_bars | 8.5748 |
| exposure | 0.4354 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
