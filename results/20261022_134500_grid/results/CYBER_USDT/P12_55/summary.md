# EMA Hourly Continuation — CYBER/USDT P12_55

**Symbol:** CYBER/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 955 |
| net_profit_factor | 0.6263 |
| net_win_rate | 0.4691 |
| gross_profit_factor | 0.9717 |
| gross_win_rate | 0.4785 |
| sharpe_ratio | -5.5264 |
| sortino_ratio | -2.4028 |
| max_drawdown | 0.9469 |
| cagr | -0.6874 |
| net_avg_win | 35.3915 |
| net_avg_loss | -49.9336 |
| avg_hold_time_bars | 9.1634 |
| exposure | 0.3978 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
