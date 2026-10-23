# EMA Hourly Continuation — W/USDT P26_50

**Symbol:** W/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 927 |
| net_profit_factor | 0.5574 |
| net_win_rate | 0.4628 |
| gross_profit_factor | 0.9623 |
| gross_win_rate | 0.4714 |
| sharpe_ratio | -6.4384 |
| sortino_ratio | -2.7502 |
| max_drawdown | 0.9677 |
| cagr | -0.7423 |
| net_avg_win | 28.3803 |
| net_avg_loss | -43.8618 |
| avg_hold_time_bars | 3.7325 |
| exposure | 0.1573 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
