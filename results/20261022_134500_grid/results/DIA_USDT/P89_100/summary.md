# EMA Hourly Continuation — DIA/USDT P89_100

**Symbol:** DIA/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 629 |
| net_profit_factor | 0.2912 |
| net_win_rate | 0.3911 |
| gross_profit_factor | 0.8144 |
| gross_win_rate | 0.4356 |
| sharpe_ratio | -9.0446 |
| sortino_ratio | -3.2475 |
| max_drawdown | 0.9861 |
| cagr | -0.8165 |
| net_avg_win | 16.4662 |
| net_avg_loss | -36.3233 |
| avg_hold_time_bars | 2.6200 |
| exposure | 0.0746 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
