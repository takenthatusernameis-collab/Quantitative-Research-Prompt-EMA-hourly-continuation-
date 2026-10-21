# EMA Hourly Continuation — ICP/USDT P34_100

**Symbol:** ICP/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 430 |
| net_profit_factor | 0.7063 |
| net_win_rate | 0.4791 |
| gross_profit_factor | 0.9059 |
| gross_win_rate | 0.4791 |
| sharpe_ratio | -2.2043 |
| sortino_ratio | -0.6520 |
| max_drawdown | 0.5430 |
| cagr | -0.2586 |
| net_avg_win | 61.6903 |
| net_avg_loss | -80.3194 |
| avg_hold_time_bars | 12.1605 |
| exposure | 0.2377 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
