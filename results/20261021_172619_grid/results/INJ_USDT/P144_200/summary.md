# EMA Hourly Continuation — INJ/USDT P144_200

**Symbol:** INJ/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 191 |
| net_profit_factor | 0.6763 |
| net_win_rate | 0.4712 |
| gross_profit_factor | 0.8723 |
| gross_win_rate | 0.4712 |
| sharpe_ratio | -1.6052 |
| sortino_ratio | -0.3165 |
| max_drawdown | 0.3295 |
| cagr | -0.1351 |
| net_avg_win | 70.8947 |
| net_avg_loss | -93.4148 |
| avg_hold_time_bars | 7.4607 |
| exposure | 0.0648 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
