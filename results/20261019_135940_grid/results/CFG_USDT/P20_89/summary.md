# EMA Hourly Continuation — CFG/USDT P20_89

**Symbol:** CFG/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 626 |
| net_profit_factor | 0.5742 |
| net_win_rate | 0.4377 |
| gross_profit_factor | 0.8301 |
| gross_win_rate | 0.4409 |
| sharpe_ratio | -4.4593 |
| sortino_ratio | -1.5736 |
| max_drawdown | 0.8503 |
| cagr | -0.5231 |
| net_avg_win | 41.5482 |
| net_avg_loss | -56.3254 |
| avg_hold_time_bars | 17.9345 |
| exposure | 0.5103 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
