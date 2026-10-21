# EMA Hourly Continuation — AKT/USDT P21_89

**Symbol:** AKT/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 479 |
| net_profit_factor | 0.8246 |
| net_win_rate | 0.5031 |
| gross_profit_factor | 1.0017 |
| gross_win_rate | 0.5031 |
| sharpe_ratio | -1.2545 |
| sortino_ratio | -0.3934 |
| max_drawdown | 0.3803 |
| cagr | -0.1675 |
| net_avg_win | 72.0002 |
| net_avg_loss | -88.4128 |
| avg_hold_time_bars | 14.9144 |
| exposure | 0.3247 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
