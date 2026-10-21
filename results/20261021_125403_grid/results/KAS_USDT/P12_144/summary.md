# EMA Hourly Continuation — KAS/USDT P12_144

**Symbol:** KAS/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 362 |
| net_profit_factor | 0.8270 |
| net_win_rate | 0.5055 |
| gross_profit_factor | 0.9983 |
| gross_win_rate | 0.5055 |
| sharpe_ratio | -1.0400 |
| sortino_ratio | -0.2831 |
| max_drawdown | 0.3364 |
| cagr | -0.1240 |
| net_avg_win | 73.9052 |
| net_avg_loss | -91.3632 |
| avg_hold_time_bars | 39.5442 |
| exposure | 0.6507 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
