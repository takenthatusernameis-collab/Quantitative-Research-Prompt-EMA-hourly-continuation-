# EMA Hourly Continuation — IO/USDT P20_100

**Symbol:** IO/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 422 |
| net_profit_factor | 0.8158 |
| net_win_rate | 0.4882 |
| gross_profit_factor | 0.9590 |
| gross_win_rate | 0.4882 |
| sharpe_ratio | -1.4096 |
| sortino_ratio | -0.4266 |
| max_drawdown | 0.4114 |
| cagr | -0.1798 |
| net_avg_win | 80.2804 |
| net_avg_loss | -93.8488 |
| avg_hold_time_bars | 20.3910 |
| exposure | 0.4166 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
