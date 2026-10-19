# EMA Hourly Continuation — AR/USDT P34_50

**Symbol:** AR/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 926 |
| net_profit_factor | 0.3248 |
| net_win_rate | 0.4233 |
| gross_profit_factor | 0.6116 |
| gross_win_rate | 0.4417 |
| sharpe_ratio | -8.4470 |
| sortino_ratio | -3.6394 |
| max_drawdown | 0.9892 |
| cagr | -0.8354 |
| net_avg_win | 12.1400 |
| net_avg_loss | -27.4366 |
| avg_hold_time_bars | 2.9438 |
| exposure | 0.1239 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
