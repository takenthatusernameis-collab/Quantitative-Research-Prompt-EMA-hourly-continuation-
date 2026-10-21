# EMA Hourly Continuation — XPR/USDT P20_55

**Symbol:** XPR/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 347 |
| net_profit_factor | 0.7801 |
| net_win_rate | 0.5101 |
| gross_profit_factor | 1.0420 |
| gross_win_rate | 0.5101 |
| sharpe_ratio | -1.4873 |
| sortino_ratio | -0.3983 |
| max_drawdown | 0.4080 |
| cagr | -0.1670 |
| net_avg_win | 73.7496 |
| net_avg_loss | -98.4376 |
| avg_hold_time_bars | 11.5620 |
| exposure | 0.1824 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
