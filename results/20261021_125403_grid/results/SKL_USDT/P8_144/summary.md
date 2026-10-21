# EMA Hourly Continuation — SKL/USDT P8_144

**Symbol:** SKL/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 381 |
| net_profit_factor | 0.9402 |
| net_win_rate | 0.5302 |
| gross_profit_factor | 1.1108 |
| gross_win_rate | 0.5302 |
| sharpe_ratio | -0.3308 |
| sortino_ratio | -0.0931 |
| max_drawdown | 0.2935 |
| cagr | -0.0470 |
| net_avg_win | 88.7057 |
| net_avg_loss | -106.4705 |
| avg_hold_time_bars | 43.3281 |
| exposure | 0.7504 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
