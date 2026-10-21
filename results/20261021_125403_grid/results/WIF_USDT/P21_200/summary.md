# EMA Hourly Continuation — WIF/USDT P21_200

**Symbol:** WIF/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 307 |
| net_profit_factor | 0.7787 |
| net_win_rate | 0.4723 |
| gross_profit_factor | 0.8877 |
| gross_win_rate | 0.4723 |
| sharpe_ratio | -1.3299 |
| sortino_ratio | -0.3313 |
| max_drawdown | 0.3387 |
| cagr | -0.1425 |
| net_avg_win | 77.6862 |
| net_avg_loss | -89.2996 |
| avg_hold_time_bars | 41.8502 |
| exposure | 0.5840 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
