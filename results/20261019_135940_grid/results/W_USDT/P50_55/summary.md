# EMA Hourly Continuation — W/USDT P50_55

**Symbol:** W/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 782 |
| net_profit_factor | 0.2641 |
| net_win_rate | 0.3760 |
| gross_profit_factor | 0.7217 |
| gross_win_rate | 0.4258 |
| sharpe_ratio | -10.9325 |
| sortino_ratio | -4.4479 |
| max_drawdown | 0.9975 |
| cagr | -0.9064 |
| net_avg_win | 12.1745 |
| net_avg_loss | -27.7730 |
| avg_hold_time_bars | 1.8798 |
| exposure | 0.0668 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
