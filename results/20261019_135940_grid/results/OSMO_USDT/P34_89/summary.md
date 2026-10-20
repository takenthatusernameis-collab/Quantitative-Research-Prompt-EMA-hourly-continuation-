# EMA Hourly Continuation — OSMO/USDT P34_89

**Symbol:** OSMO/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 689 |
| net_profit_factor | 0.5825 |
| net_win_rate | 0.4470 |
| gross_profit_factor | 0.9731 |
| gross_win_rate | 0.4630 |
| sharpe_ratio | -5.2411 |
| sortino_ratio | -1.9505 |
| max_drawdown | 0.9020 |
| cagr | -0.6007 |
| net_avg_win | 40.7889 |
| net_avg_loss | -56.6031 |
| avg_hold_time_bars | 8.1030 |
| exposure | 0.2538 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
