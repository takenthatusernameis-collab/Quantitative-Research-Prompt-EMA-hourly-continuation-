# EMA Hourly Continuation — OSMO/USDT P12_89

**Symbol:** OSMO/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 740 |
| net_profit_factor | 0.6874 |
| net_win_rate | 0.4770 |
| gross_profit_factor | 1.0433 |
| gross_win_rate | 0.4919 |
| sharpe_ratio | -3.9290 |
| sortino_ratio | -1.5148 |
| max_drawdown | 0.8405 |
| cagr | -0.5088 |
| net_avg_win | 51.8491 |
| net_avg_loss | -68.7987 |
| avg_hold_time_bars | 15.8716 |
| exposure | 0.5339 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
