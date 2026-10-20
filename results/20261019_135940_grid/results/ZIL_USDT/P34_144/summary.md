# EMA Hourly Continuation — ZIL/USDT P34_144

**Symbol:** ZIL/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 498 |
| net_profit_factor | 0.6605 |
| net_win_rate | 0.4900 |
| gross_profit_factor | 0.9982 |
| gross_win_rate | 0.5000 |
| sharpe_ratio | -2.9168 |
| sortino_ratio | -0.9247 |
| max_drawdown | 0.6904 |
| cagr | -0.3512 |
| net_avg_win | 52.8205 |
| net_avg_loss | -76.8276 |
| avg_hold_time_bars | 17.8052 |
| exposure | 0.4030 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
