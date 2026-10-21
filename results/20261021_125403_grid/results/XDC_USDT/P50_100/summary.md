# EMA Hourly Continuation — XDC/USDT P50_100

**Symbol:** XDC/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 339 |
| net_profit_factor | 0.7199 |
| net_win_rate | 0.5251 |
| gross_profit_factor | 1.1011 |
| gross_win_rate | 0.5251 |
| sharpe_ratio | -1.8373 |
| sortino_ratio | -0.4883 |
| max_drawdown | 0.4444 |
| cagr | -0.1991 |
| net_avg_win | 61.7188 |
| net_avg_loss | -94.7787 |
| avg_hold_time_bars | 8.5959 |
| exposure | 0.1325 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
