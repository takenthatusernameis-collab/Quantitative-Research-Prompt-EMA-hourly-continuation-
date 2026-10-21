# EMA Hourly Continuation — GMT/USDT P34_100

**Symbol:** GMT/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 427 |
| net_profit_factor | 0.7009 |
| net_win_rate | 0.4707 |
| gross_profit_factor | 0.9026 |
| gross_win_rate | 0.4707 |
| sharpe_ratio | -2.4139 |
| sortino_ratio | -0.7111 |
| max_drawdown | 0.5782 |
| cagr | -0.2786 |
| net_avg_win | 65.2377 |
| net_avg_loss | -82.7813 |
| avg_hold_time_bars | 12.9696 |
| exposure | 0.2517 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
