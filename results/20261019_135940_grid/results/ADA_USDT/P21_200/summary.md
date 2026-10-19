# EMA Hourly Continuation — ADA/USDT P21_200

**Symbol:** ADA/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 363 |
| net_profit_factor | 0.6205 |
| net_win_rate | 0.4848 |
| gross_profit_factor | 0.9662 |
| gross_win_rate | 0.4931 |
| sharpe_ratio | -2.7877 |
| sortino_ratio | -0.7368 |
| max_drawdown | 0.6175 |
| cagr | -0.3060 |
| net_avg_win | 55.7721 |
| net_avg_loss | -84.5969 |
| avg_hold_time_bars | 37.3912 |
| exposure | 0.6170 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
