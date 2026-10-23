# EMA Hourly Continuation — XNO/USDT P8_34

**Symbol:** XNO/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1542 |
| net_profit_factor | 0.4547 |
| net_win_rate | 0.3885 |
| gross_profit_factor | 0.8261 |
| gross_win_rate | 0.4060 |
| sharpe_ratio | -11.8299 |
| sortino_ratio | -6.5650 |
| max_drawdown | 0.9997 |
| cagr | -0.9608 |
| net_avg_win | 13.9194 |
| net_avg_loss | -19.4430 |
| avg_hold_time_bars | 4.5921 |
| exposure | 0.3219 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
