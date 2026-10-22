# EMA Hourly Continuation — SKL/USDT P20_50

**Symbol:** SKL/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 526 |
| net_profit_factor | 0.6918 |
| net_win_rate | 0.4715 |
| gross_profit_factor | 0.9146 |
| gross_win_rate | 0.4715 |
| sharpe_ratio | -2.8891 |
| sortino_ratio | -0.9458 |
| max_drawdown | 0.6808 |
| cagr | -0.3518 |
| net_avg_win | 60.0394 |
| net_avg_loss | -77.4227 |
| avg_hold_time_bars | 7.7338 |
| exposure | 0.1849 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
