# EMA Hourly Continuation — IO/USDT P20_34

**Symbol:** IO/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 285 |
| net_profit_factor | 0.8292 |
| net_win_rate | 0.5123 |
| gross_profit_factor | 1.0500 |
| gross_win_rate | 0.5123 |
| sharpe_ratio | -1.0327 |
| sortino_ratio | -0.2587 |
| max_drawdown | 0.2664 |
| cagr | -0.1131 |
| net_avg_win | 81.9600 |
| net_avg_loss | -103.8145 |
| avg_hold_time_bars | 5.4035 |
| exposure | 0.0746 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
