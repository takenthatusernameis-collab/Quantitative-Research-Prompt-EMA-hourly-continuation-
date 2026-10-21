# EMA Hourly Continuation — AKT/USDT P8_89

**Symbol:** AKT/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 518 |
| net_profit_factor | 0.8721 |
| net_win_rate | 0.5077 |
| gross_profit_factor | 1.0292 |
| gross_win_rate | 0.5077 |
| sharpe_ratio | -0.9750 |
| sortino_ratio | -0.3182 |
| max_drawdown | 0.3612 |
| cagr | -0.1401 |
| net_avg_win | 81.7566 |
| net_avg_loss | -96.6913 |
| avg_hold_time_bars | 24.8378 |
| exposure | 0.5848 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
