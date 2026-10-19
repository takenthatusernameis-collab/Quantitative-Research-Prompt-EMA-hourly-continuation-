# EMA Hourly Continuation — JST/USDT P8_20

**Symbol:** JST/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1378 |
| net_profit_factor | 0.1369 |
| net_win_rate | 0.3687 |
| gross_profit_factor | 0.6716 |
| gross_win_rate | 0.4543 |
| sharpe_ratio | -15.7956 |
| sortino_ratio | -8.5768 |
| max_drawdown | 1.0000 |
| cagr | -0.9903 |
| net_avg_win | 3.1233 |
| net_avg_loss | -13.3179 |
| avg_hold_time_bars | 3.6495 |
| exposure | 0.2276 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
