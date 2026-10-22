# EMA Hourly Continuation — RPL/USDT P55_100

**Symbol:** RPL/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 411 |
| net_profit_factor | 0.6961 |
| net_win_rate | 0.4769 |
| gross_profit_factor | 0.9284 |
| gross_win_rate | 0.4769 |
| sharpe_ratio | -2.4207 |
| sortino_ratio | -0.6995 |
| max_drawdown | 0.5635 |
| cagr | -0.2734 |
| net_avg_win | 64.6336 |
| net_avg_loss | -84.6507 |
| avg_hold_time_bars | 9.9100 |
| exposure | 0.1843 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
