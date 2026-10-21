# EMA Hourly Continuation — KAS/USDT P8_55

**Symbol:** KAS/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 657 |
| net_profit_factor | 0.8484 |
| net_win_rate | 0.5205 |
| gross_profit_factor | 1.0670 |
| gross_win_rate | 0.5205 |
| sharpe_ratio | -1.2180 |
| sortino_ratio | -0.4494 |
| max_drawdown | 0.4531 |
| cagr | -0.1901 |
| net_avg_win | 67.2498 |
| net_avg_loss | -86.0643 |
| avg_hold_time_bars | 14.9680 |
| exposure | 0.4470 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
