# EMA Hourly Continuation — LTC/USDT P20_50

**Symbol:** LTC/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 439 |
| net_profit_factor | 0.6606 |
| net_win_rate | 0.5034 |
| gross_profit_factor | 0.9949 |
| gross_win_rate | 0.5034 |
| sharpe_ratio | -2.6000 |
| sortino_ratio | -0.7843 |
| max_drawdown | 0.6186 |
| cagr | -0.3001 |
| net_avg_win | 52.1109 |
| net_avg_loss | -79.9748 |
| avg_hold_time_bars | 7.2005 |
| exposure | 0.1437 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
