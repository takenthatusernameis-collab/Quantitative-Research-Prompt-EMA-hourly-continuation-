# EMA Hourly Continuation — LISTA/USDT P8_200

**Symbol:** LISTA/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 331 |
| net_profit_factor | 0.8966 |
| net_win_rate | 0.5106 |
| gross_profit_factor | 1.0556 |
| gross_win_rate | 0.5166 |
| sharpe_ratio | -0.5865 |
| sortino_ratio | -0.1587 |
| max_drawdown | 0.2070 |
| cagr | -0.0741 |
| net_avg_win | 84.4070 |
| net_avg_loss | -98.2074 |
| avg_hold_time_bars | 45.8459 |
| exposure | 0.7420 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
