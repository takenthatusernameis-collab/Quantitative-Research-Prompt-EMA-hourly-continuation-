# EMA Hourly Continuation — IMX/USDT P21_89

**Symbol:** IMX/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 486 |
| net_profit_factor | 0.8576 |
| net_win_rate | 0.5123 |
| gross_profit_factor | 1.0416 |
| gross_win_rate | 0.5123 |
| sharpe_ratio | -0.9861 |
| sortino_ratio | -0.3115 |
| max_drawdown | 0.3233 |
| cagr | -0.1365 |
| net_avg_win | 74.7839 |
| net_avg_loss | -91.6220 |
| avg_hold_time_bars | 17.1337 |
| exposure | 0.3768 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
