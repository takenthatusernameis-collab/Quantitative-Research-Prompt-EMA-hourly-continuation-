# EMA Hourly Continuation — ATH/USDT P50_100

**Symbol:** ATH/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 318 |
| net_profit_factor | 0.8139 |
| net_win_rate | 0.5126 |
| gross_profit_factor | 1.0317 |
| gross_win_rate | 0.5126 |
| sharpe_ratio | -1.1035 |
| sortino_ratio | -0.2917 |
| max_drawdown | 0.2883 |
| cagr | -0.1265 |
| net_avg_win | 73.1757 |
| net_avg_loss | -94.5527 |
| avg_hold_time_bars | 9.3994 |
| exposure | 0.1449 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
