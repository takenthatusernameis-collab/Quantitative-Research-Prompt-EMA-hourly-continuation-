# EMA Hourly Continuation — MEW/USDT P144_200

**Symbol:** MEW/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 207 |
| net_profit_factor | 0.7365 |
| net_win_rate | 0.4928 |
| gross_profit_factor | 0.9559 |
| gross_win_rate | 0.4928 |
| sharpe_ratio | -1.3505 |
| sortino_ratio | -0.2782 |
| max_drawdown | 0.3648 |
| cagr | -0.1201 |
| net_avg_win | 75.2892 |
| net_avg_loss | -99.3108 |
| avg_hold_time_bars | 6.6667 |
| exposure | 0.0627 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
