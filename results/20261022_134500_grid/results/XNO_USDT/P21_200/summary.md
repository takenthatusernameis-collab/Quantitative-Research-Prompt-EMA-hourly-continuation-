# EMA Hourly Continuation — XNO/USDT P21_200

**Symbol:** XNO/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 564 |
| net_profit_factor | 0.5739 |
| net_win_rate | 0.4468 |
| gross_profit_factor | 0.8149 |
| gross_win_rate | 0.4486 |
| sharpe_ratio | -4.2023 |
| sortino_ratio | -1.4105 |
| max_drawdown | 0.8117 |
| cagr | -0.4857 |
| net_avg_win | 43.3835 |
| net_avg_loss | -61.0562 |
| avg_hold_time_bars | 22.1259 |
| exposure | 0.5672 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
