# EMA Hourly Continuation — ENS/USDT P8_26

**Symbol:** ENS/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 683 |
| net_profit_factor | 0.7480 |
| net_win_rate | 0.5037 |
| gross_profit_factor | 1.0102 |
| gross_win_rate | 0.5037 |
| sharpe_ratio | -2.5065 |
| sortino_ratio | -0.9404 |
| max_drawdown | 0.6750 |
| cagr | -0.3500 |
| net_avg_win | 57.0256 |
| net_avg_loss | -77.3657 |
| avg_hold_time_bars | 7.1918 |
| exposure | 0.2233 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
