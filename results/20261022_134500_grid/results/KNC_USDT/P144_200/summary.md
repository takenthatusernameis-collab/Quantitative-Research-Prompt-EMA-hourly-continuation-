# EMA Hourly Continuation — KNC/USDT P144_200

**Symbol:** KNC/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 368 |
| net_profit_factor | 0.4463 |
| net_win_rate | 0.4457 |
| gross_profit_factor | 0.9546 |
| gross_win_rate | 0.4918 |
| sharpe_ratio | -4.9311 |
| sortino_ratio | -1.3231 |
| max_drawdown | 0.8222 |
| cagr | -0.4968 |
| net_avg_win | 40.3886 |
| net_avg_loss | -72.7518 |
| avg_hold_time_bars | 5.7364 |
| exposure | 0.0960 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
