# EMA Hourly Continuation — MEW/USDT P21_26

**Symbol:** MEW/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 218 |
| net_profit_factor | 0.5733 |
| net_win_rate | 0.4450 |
| gross_profit_factor | 0.8042 |
| gross_win_rate | 0.4450 |
| sharpe_ratio | -2.6291 |
| sortino_ratio | -0.5538 |
| max_drawdown | 0.4828 |
| cagr | -0.2252 |
| net_avg_win | 65.5093 |
| net_avg_loss | -91.6094 |
| avg_hold_time_bars | 4.5183 |
| exposure | 0.0448 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
