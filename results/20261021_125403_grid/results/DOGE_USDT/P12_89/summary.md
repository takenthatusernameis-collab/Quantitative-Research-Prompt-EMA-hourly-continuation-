# EMA Hourly Continuation — DOGE/USDT P12_89

**Symbol:** DOGE/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 491 |
| net_profit_factor | 0.7589 |
| net_win_rate | 0.4908 |
| gross_profit_factor | 0.9666 |
| gross_win_rate | 0.4908 |
| sharpe_ratio | -1.9945 |
| sortino_ratio | -0.6313 |
| max_drawdown | 0.5387 |
| cagr | -0.2528 |
| net_avg_win | 67.7805 |
| net_avg_loss | -86.0979 |
| avg_hold_time_bars | 22.0367 |
| exposure | 0.4918 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
