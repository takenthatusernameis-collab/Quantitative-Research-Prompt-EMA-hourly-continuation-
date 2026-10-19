# EMA Hourly Continuation — WLD/USDT P20_200

**Symbol:** WLD/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 295 |
| net_profit_factor | 0.9523 |
| net_win_rate | 0.5390 |
| gross_profit_factor | 1.1532 |
| gross_win_rate | 0.5390 |
| sharpe_ratio | -0.1979 |
| sortino_ratio | -0.0487 |
| max_drawdown | 0.2405 |
| cagr | -0.0275 |
| net_avg_win | 84.7960 |
| net_avg_loss | -104.1009 |
| avg_hold_time_bars | 50.2034 |
| exposure | 0.6732 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
