# EMA Hourly Continuation — MEW/USDT P21_200

**Symbol:** MEW/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 294 |
| net_profit_factor | 0.8505 |
| net_win_rate | 0.4966 |
| gross_profit_factor | 0.9789 |
| gross_win_rate | 0.4966 |
| sharpe_ratio | -0.8228 |
| sortino_ratio | -0.2015 |
| max_drawdown | 0.3179 |
| cagr | -0.0908 |
| net_avg_win | 82.8951 |
| net_avg_loss | -96.1444 |
| avg_hold_time_bars | 46.6667 |
| exposure | 0.6236 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
