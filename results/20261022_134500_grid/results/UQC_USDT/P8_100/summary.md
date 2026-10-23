# EMA Hourly Continuation — UQC/USDT P8_100

**Symbol:** UQC/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 285 |
| net_profit_factor | 0.3990 |
| net_win_rate | 0.3228 |
| gross_profit_factor | 0.5922 |
| gross_win_rate | 0.3368 |
| sharpe_ratio | -5.9088 |
| sortino_ratio | -1.3825 |
| max_drawdown | 0.8381 |
| cagr | -0.5129 |
| net_avg_win | 60.3920 |
| net_avg_loss | -72.1576 |
| avg_hold_time_bars | 55.6772 |
| exposure | 0.7182 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
