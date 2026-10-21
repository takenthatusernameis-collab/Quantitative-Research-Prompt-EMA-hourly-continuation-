# EMA Hourly Continuation — WLD/USDT P89_100

**Symbol:** WLD/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 75 |
| net_profit_factor | 0.8813 |
| net_win_rate | 0.5333 |
| gross_profit_factor | 1.1344 |
| gross_win_rate | 0.5333 |
| sharpe_ratio | -0.3223 |
| sortino_ratio | -0.0404 |
| max_drawdown | 0.1036 |
| cagr | -0.0189 |
| net_avg_win | 87.0790 |
| net_avg_loss | -112.9190 |
| avg_hold_time_bars | 5.6667 |
| exposure | 0.0193 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
