# EMA Hourly Continuation — SNX/USDT P26_34

**Symbol:** SNX/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 193 |
| net_profit_factor | 0.7242 |
| net_win_rate | 0.5130 |
| gross_profit_factor | 1.0412 |
| gross_win_rate | 0.5130 |
| sharpe_ratio | -1.3482 |
| sortino_ratio | -0.2694 |
| max_drawdown | 0.2997 |
| cagr | -0.1155 |
| net_avg_win | 70.6052 |
| net_avg_loss | -102.6845 |
| avg_hold_time_bars | 4.2383 |
| exposure | 0.0370 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
