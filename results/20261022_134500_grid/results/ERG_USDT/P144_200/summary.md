# EMA Hourly Continuation — ERG/USDT P144_200

**Symbol:** ERG/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 449 |
| net_profit_factor | 0.3153 |
| net_win_rate | 0.3474 |
| gross_profit_factor | 0.5772 |
| gross_win_rate | 0.3563 |
| sharpe_ratio | -7.5745 |
| sortino_ratio | -2.3164 |
| max_drawdown | 0.9436 |
| cagr | -0.6777 |
| net_avg_win | 27.7952 |
| net_avg_loss | -46.9408 |
| avg_hold_time_bars | 3.9310 |
| exposure | 0.0802 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
