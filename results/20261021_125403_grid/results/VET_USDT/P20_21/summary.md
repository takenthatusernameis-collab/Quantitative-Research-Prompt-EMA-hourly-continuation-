# EMA Hourly Continuation — VET/USDT P20_21

**Symbol:** VET/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 131 |
| net_profit_factor | 0.7650 |
| net_win_rate | 0.5344 |
| gross_profit_factor | 1.1449 |
| gross_win_rate | 0.5344 |
| sharpe_ratio | -0.9554 |
| sortino_ratio | -0.1583 |
| max_drawdown | 0.2275 |
| cagr | -0.0699 |
| net_avg_win | 77.4091 |
| net_avg_loss | -116.1128 |
| avg_hold_time_bars | 5.0382 |
| exposure | 0.0300 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
