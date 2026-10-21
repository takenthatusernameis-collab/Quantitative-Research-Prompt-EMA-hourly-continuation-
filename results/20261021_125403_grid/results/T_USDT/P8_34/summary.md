# EMA Hourly Continuation — T/USDT P8_34

**Symbol:** T/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 790 |
| net_profit_factor | 0.7006 |
| net_win_rate | 0.4848 |
| gross_profit_factor | 1.0174 |
| gross_win_rate | 0.4886 |
| sharpe_ratio | -3.8235 |
| sortino_ratio | -1.5353 |
| max_drawdown | 0.8345 |
| cagr | -0.5041 |
| net_avg_win | 50.6887 |
| net_avg_loss | -68.0817 |
| avg_hold_time_bars | 9.1772 |
| exposure | 0.3281 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
