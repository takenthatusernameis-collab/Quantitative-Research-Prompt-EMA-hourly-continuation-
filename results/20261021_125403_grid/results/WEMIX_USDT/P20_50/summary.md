# EMA Hourly Continuation — WEMIX/USDT P20_50

**Symbol:** WEMIX/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 372 |
| net_profit_factor | 0.5737 |
| net_win_rate | 0.4247 |
| gross_profit_factor | 0.7648 |
| gross_win_rate | 0.4247 |
| sharpe_ratio | -3.6450 |
| sortino_ratio | -0.9968 |
| max_drawdown | 0.6919 |
| cagr | -0.3699 |
| net_avg_win | 58.4715 |
| net_avg_loss | -75.2509 |
| avg_hold_time_bars | 11.5618 |
| exposure | 0.1955 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
