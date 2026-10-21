# EMA Hourly Continuation — AVAX/USDT P89_100

**Symbol:** AVAX/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 78 |
| net_profit_factor | 0.6867 |
| net_win_rate | 0.5000 |
| gross_profit_factor | 0.9933 |
| gross_win_rate | 0.5000 |
| sharpe_ratio | -1.0168 |
| sortino_ratio | -0.1292 |
| max_drawdown | 0.1447 |
| cagr | -0.0575 |
| net_avg_win | 77.6890 |
| net_avg_loss | -113.1394 |
| avg_hold_time_bars | 4.3462 |
| exposure | 0.0154 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
