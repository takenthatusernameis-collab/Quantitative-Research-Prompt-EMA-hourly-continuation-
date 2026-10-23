# EMA Hourly Continuation — ILV/USDT P20_100

**Symbol:** ILV/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 676 |
| net_profit_factor | 0.6868 |
| net_win_rate | 0.4911 |
| gross_profit_factor | 1.0095 |
| gross_win_rate | 0.4985 |
| sharpe_ratio | -3.3089 |
| sortino_ratio | -1.2203 |
| max_drawdown | 0.7701 |
| cagr | -0.4360 |
| net_avg_win | 50.3798 |
| net_avg_loss | -70.7933 |
| avg_hold_time_bars | 13.5680 |
| exposure | 0.4169 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
