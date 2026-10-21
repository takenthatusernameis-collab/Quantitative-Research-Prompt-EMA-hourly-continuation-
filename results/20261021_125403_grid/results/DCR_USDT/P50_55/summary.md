# EMA Hourly Continuation — DCR/USDT P50_55

**Symbol:** DCR/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 203 |
| net_profit_factor | 0.4883 |
| net_win_rate | 0.4532 |
| gross_profit_factor | 0.8140 |
| gross_win_rate | 0.4532 |
| sharpe_ratio | -3.0242 |
| sortino_ratio | -0.6170 |
| max_drawdown | 0.5201 |
| cagr | -0.2499 |
| net_avg_win | 53.5150 |
| net_avg_loss | -90.8333 |
| avg_hold_time_bars | 5.3300 |
| exposure | 0.0490 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
