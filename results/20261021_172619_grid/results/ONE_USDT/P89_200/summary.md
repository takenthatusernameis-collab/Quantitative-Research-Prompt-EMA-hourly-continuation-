# EMA Hourly Continuation — ONE/USDT P89_200

**Symbol:** ONE/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 265 |
| net_profit_factor | 0.7683 |
| net_win_rate | 0.4792 |
| gross_profit_factor | 0.9355 |
| gross_win_rate | 0.4792 |
| sharpe_ratio | -1.4027 |
| sortino_ratio | -0.3256 |
| max_drawdown | 0.3343 |
| cagr | -0.1394 |
| net_avg_win | 82.0139 |
| net_avg_loss | -98.2337 |
| avg_hold_time_bars | 18.9057 |
| exposure | 0.2277 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
