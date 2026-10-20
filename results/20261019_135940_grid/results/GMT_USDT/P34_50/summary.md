# EMA Hourly Continuation — GMT/USDT P34_50

**Symbol:** GMT/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 934 |
| net_profit_factor | 0.3777 |
| net_win_rate | 0.4122 |
| gross_profit_factor | 0.8547 |
| gross_win_rate | 0.4325 |
| sharpe_ratio | -9.8977 |
| sortino_ratio | -4.3117 |
| max_drawdown | 0.9961 |
| cagr | -0.8880 |
| net_avg_win | 15.6991 |
| net_avg_loss | -29.1497 |
| avg_hold_time_bars | 2.7709 |
| exposure | 0.1176 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
