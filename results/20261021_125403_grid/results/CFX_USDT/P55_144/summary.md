# EMA Hourly Continuation — CFX/USDT P55_144

**Symbol:** CFX/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 310 |
| net_profit_factor | 0.8008 |
| net_win_rate | 0.5065 |
| gross_profit_factor | 1.0055 |
| gross_win_rate | 0.5065 |
| sharpe_ratio | -1.1235 |
| sortino_ratio | -0.2839 |
| max_drawdown | 0.3001 |
| cagr | -0.1231 |
| net_avg_win | 71.9820 |
| net_avg_loss | -92.2358 |
| avg_hold_time_bars | 18.7645 |
| exposure | 0.2644 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
