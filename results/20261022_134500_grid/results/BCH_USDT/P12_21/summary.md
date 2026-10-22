# EMA Hourly Continuation — BCH/USDT P12_21

**Symbol:** BCH/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1402 |
| net_profit_factor | 0.1803 |
| net_win_rate | 0.3573 |
| gross_profit_factor | 0.6488 |
| gross_win_rate | 0.4080 |
| sharpe_ratio | -16.3833 |
| sortino_ratio | -8.9860 |
| max_drawdown | 1.0000 |
| cagr | -0.9923 |
| net_avg_win | 4.3918 |
| net_avg_loss | -13.5408 |
| avg_hold_time_bars | 2.2539 |
| exposure | 0.1436 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
