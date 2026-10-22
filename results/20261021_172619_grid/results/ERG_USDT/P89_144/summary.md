# EMA Hourly Continuation — ERG/USDT P89_144

**Symbol:** ERG/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 215 |
| net_profit_factor | 0.5170 |
| net_win_rate | 0.4140 |
| gross_profit_factor | 0.7043 |
| gross_win_rate | 0.4140 |
| sharpe_ratio | -2.9609 |
| sortino_ratio | -0.6165 |
| max_drawdown | 0.5137 |
| cagr | -0.2472 |
| net_avg_win | 61.3150 |
| net_avg_loss | -83.7701 |
| avg_hold_time_bars | 9.0884 |
| exposure | 0.0888 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
