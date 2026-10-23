# EMA Hourly Continuation — MEW/USDT P8_12

**Symbol:** MEW/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1764 |
| net_profit_factor | 0.4203 |
| net_win_rate | 0.3764 |
| gross_profit_factor | 0.8379 |
| gross_win_rate | 0.4172 |
| sharpe_ratio | -15.5146 |
| sortino_ratio | -9.3264 |
| max_drawdown | 1.0000 |
| cagr | -0.9919 |
| net_avg_win | 10.9182 |
| net_avg_loss | -15.6815 |
| avg_hold_time_bars | 1.8673 |
| exposure | 0.1497 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
