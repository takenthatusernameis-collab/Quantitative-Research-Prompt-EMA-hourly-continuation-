# EMA Hourly Continuation — ERG/USDT P50_144

**Symbol:** ERG/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 336 |
| net_profit_factor | 0.5815 |
| net_win_rate | 0.4226 |
| gross_profit_factor | 0.7392 |
| gross_win_rate | 0.4226 |
| sharpe_ratio | -3.1502 |
| sortino_ratio | -0.8169 |
| max_drawdown | 0.6117 |
| cagr | -0.3138 |
| net_avg_win | 59.8568 |
| net_avg_loss | -75.3421 |
| avg_hold_time_bars | 16.3006 |
| exposure | 0.2490 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
