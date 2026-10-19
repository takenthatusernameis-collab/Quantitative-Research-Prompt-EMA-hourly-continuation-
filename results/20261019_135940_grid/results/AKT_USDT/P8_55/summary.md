# EMA Hourly Continuation — AKT/USDT P8_55

**Symbol:** AKT/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1030 |
| net_profit_factor | 0.5368 |
| net_win_rate | 0.4680 |
| gross_profit_factor | 0.8807 |
| gross_win_rate | 0.4748 |
| sharpe_ratio | -5.4860 |
| sortino_ratio | -2.4752 |
| max_drawdown | 0.9510 |
| cagr | -0.6955 |
| net_avg_win | 22.8318 |
| net_avg_loss | -37.4090 |
| avg_hold_time_bars | 9.9631 |
| exposure | 0.4665 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
