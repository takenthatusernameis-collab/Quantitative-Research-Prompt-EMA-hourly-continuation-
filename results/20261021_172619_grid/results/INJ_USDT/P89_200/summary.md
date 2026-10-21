# EMA Hourly Continuation — INJ/USDT P89_200

**Symbol:** INJ/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 254 |
| net_profit_factor | 0.7201 |
| net_win_rate | 0.4724 |
| gross_profit_factor | 0.8806 |
| gross_win_rate | 0.4724 |
| sharpe_ratio | -1.5702 |
| sortino_ratio | -0.3564 |
| max_drawdown | 0.3541 |
| cagr | -0.1514 |
| net_avg_win | 72.4595 |
| net_avg_loss | -90.1091 |
| avg_hold_time_bars | 15.1732 |
| exposure | 0.1752 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
