# EMA Hourly Continuation — JUP/USDT P89_100

**Symbol:** JUP/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 83 |
| net_profit_factor | 0.6209 |
| net_win_rate | 0.4578 |
| gross_profit_factor | 0.8295 |
| gross_win_rate | 0.4578 |
| sharpe_ratio | -1.3041 |
| sortino_ratio | -0.1695 |
| max_drawdown | 0.1921 |
| cagr | -0.0749 |
| net_avg_win | 76.5505 |
| net_avg_loss | -104.1118 |
| avg_hold_time_bars | 4.2892 |
| exposure | 0.0162 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
