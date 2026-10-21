# EMA Hourly Continuation — WIF/USDT P89_100

**Symbol:** WIF/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 84 |
| net_profit_factor | 0.7148 |
| net_win_rate | 0.4762 |
| gross_profit_factor | 0.9040 |
| gross_win_rate | 0.4762 |
| sharpe_ratio | -0.9501 |
| sortino_ratio | -0.1242 |
| max_drawdown | 0.1695 |
| cagr | -0.0557 |
| net_avg_win | 83.9209 |
| net_avg_loss | -106.7386 |
| avg_hold_time_bars | 6.1429 |
| exposure | 0.0235 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
