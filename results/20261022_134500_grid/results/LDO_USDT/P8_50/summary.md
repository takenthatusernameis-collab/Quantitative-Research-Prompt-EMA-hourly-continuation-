# EMA Hourly Continuation — LDO/USDT P8_50

**Symbol:** LDO/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1141 |
| net_profit_factor | 0.5298 |
| net_win_rate | 0.4487 |
| gross_profit_factor | 0.8242 |
| gross_win_rate | 0.4584 |
| sharpe_ratio | -6.8365 |
| sortino_ratio | -3.2301 |
| max_drawdown | 0.9813 |
| cagr | -0.7946 |
| net_avg_win | 21.5930 |
| net_avg_loss | -33.1763 |
| avg_hold_time_bars | 8.7677 |
| exposure | 0.4547 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
