# EMA Hourly Continuation — ONE/USDT P89_100

**Symbol:** ONE/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 610 |
| net_profit_factor | 0.3362 |
| net_win_rate | 0.3885 |
| gross_profit_factor | 0.8918 |
| gross_win_rate | 0.4262 |
| sharpe_ratio | -9.0398 |
| sortino_ratio | -3.2193 |
| max_drawdown | 0.9851 |
| cagr | -0.8123 |
| net_avg_win | 21.0542 |
| net_avg_loss | -39.7856 |
| avg_hold_time_bars | 2.2082 |
| exposure | 0.0612 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
