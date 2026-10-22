# EMA Hourly Continuation — ERG/USDT P8_144

**Symbol:** ERG/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 466 |
| net_profit_factor | 0.6891 |
| net_win_rate | 0.4635 |
| gross_profit_factor | 0.8386 |
| gross_win_rate | 0.4635 |
| sharpe_ratio | -2.3388 |
| sortino_ratio | -0.7170 |
| max_drawdown | 0.5752 |
| cagr | -0.2817 |
| net_avg_win | 57.9059 |
| net_avg_loss | -72.6043 |
| avg_hold_time_bars | 30.9399 |
| exposure | 0.6554 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
