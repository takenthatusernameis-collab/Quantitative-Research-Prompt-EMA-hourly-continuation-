# EMA Hourly Continuation — ICP/USDT P12_100

**Symbol:** ICP/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 443 |
| net_profit_factor | 0.7978 |
| net_win_rate | 0.4966 |
| gross_profit_factor | 0.9792 |
| gross_win_rate | 0.4966 |
| sharpe_ratio | -1.4702 |
| sortino_ratio | -0.4422 |
| max_drawdown | 0.4297 |
| cagr | -0.1856 |
| net_avg_win | 72.2393 |
| net_avg_loss | -89.3307 |
| avg_hold_time_bars | 30.1264 |
| exposure | 0.6066 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
