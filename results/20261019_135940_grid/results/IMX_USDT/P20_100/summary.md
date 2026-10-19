# EMA Hourly Continuation — IMX/USDT P20_100

**Symbol:** IMX/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 611 |
| net_profit_factor | 0.6611 |
| net_win_rate | 0.4926 |
| gross_profit_factor | 0.9500 |
| gross_win_rate | 0.4992 |
| sharpe_ratio | -2.8345 |
| sortino_ratio | -0.9846 |
| max_drawdown | 0.7000 |
| cagr | -0.3750 |
| net_avg_win | 45.0156 |
| net_avg_loss | -66.1112 |
| avg_hold_time_bars | 15.6890 |
| exposure | 0.4338 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
