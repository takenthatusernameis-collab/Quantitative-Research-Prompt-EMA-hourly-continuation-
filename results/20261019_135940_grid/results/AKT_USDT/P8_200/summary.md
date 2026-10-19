# EMA Hourly Continuation — AKT/USDT P8_200

**Symbol:** AKT/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 448 |
| net_profit_factor | 0.6984 |
| net_win_rate | 0.4978 |
| gross_profit_factor | 0.9804 |
| gross_win_rate | 0.4978 |
| sharpe_ratio | -2.2731 |
| sortino_ratio | -0.6702 |
| max_drawdown | 0.5858 |
| cagr | -0.2802 |
| net_avg_win | 58.3700 |
| net_avg_loss | -82.8319 |
| avg_hold_time_bars | 37.6250 |
| exposure | 0.7662 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
