# EMA Hourly Continuation — ERG/USDT P8_50

**Symbol:** ERG/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1229 |
| net_profit_factor | 0.4123 |
| net_win_rate | 0.3922 |
| gross_profit_factor | 0.6735 |
| gross_win_rate | 0.4011 |
| sharpe_ratio | -10.1802 |
| sortino_ratio | -5.0357 |
| max_drawdown | 0.9982 |
| cagr | -0.9179 |
| net_avg_win | 14.5299 |
| net_avg_loss | -22.7371 |
| avg_hold_time_bars | 7.6021 |
| exposure | 0.4247 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
