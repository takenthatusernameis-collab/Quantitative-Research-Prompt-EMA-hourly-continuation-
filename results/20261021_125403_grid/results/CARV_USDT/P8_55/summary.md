# EMA Hourly Continuation — CARV/USDT P8_55

**Symbol:** CARV/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 568 |
| net_profit_factor | 0.8302 |
| net_win_rate | 0.5158 |
| gross_profit_factor | 1.0794 |
| gross_win_rate | 0.5176 |
| sharpe_ratio | -1.6181 |
| sortino_ratio | -0.6167 |
| max_drawdown | 0.4804 |
| cagr | -0.2483 |
| net_avg_win | 73.3418 |
| net_avg_loss | -94.1233 |
| avg_hold_time_bars | 15.1690 |
| exposure | 0.4849 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
