# EMA Hourly Continuation — VET/USDT P144_200

**Symbol:** VET/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 380 |
| net_profit_factor | 0.4156 |
| net_win_rate | 0.4263 |
| gross_profit_factor | 0.8279 |
| gross_win_rate | 0.4526 |
| sharpe_ratio | -5.3439 |
| sortino_ratio | -1.4816 |
| max_drawdown | 0.8430 |
| cagr | -0.5186 |
| net_avg_win | 36.8933 |
| net_avg_loss | -65.9716 |
| avg_hold_time_bars | 4.3184 |
| exposure | 0.0746 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
