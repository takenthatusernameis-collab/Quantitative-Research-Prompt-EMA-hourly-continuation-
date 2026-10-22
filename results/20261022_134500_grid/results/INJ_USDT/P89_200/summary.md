# EMA Hourly Continuation — INJ/USDT P89_200

**Symbol:** INJ/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 380 |
| net_profit_factor | 0.4861 |
| net_win_rate | 0.4368 |
| gross_profit_factor | 0.7302 |
| gross_win_rate | 0.4395 |
| sharpe_ratio | -3.9732 |
| sortino_ratio | -1.0861 |
| max_drawdown | 0.7443 |
| cagr | -0.4112 |
| net_avg_win | 41.9080 |
| net_avg_loss | -66.8790 |
| avg_hold_time_bars | 10.7158 |
| exposure | 0.1851 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
