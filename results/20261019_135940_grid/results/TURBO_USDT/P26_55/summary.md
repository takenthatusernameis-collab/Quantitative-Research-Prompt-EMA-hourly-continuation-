# EMA Hourly Continuation — TURBO/USDT P26_55

**Symbol:** TURBO/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 783 |
| net_profit_factor | 0.6156 |
| net_win_rate | 0.4866 |
| gross_profit_factor | 1.0057 |
| gross_win_rate | 0.4981 |
| sharpe_ratio | -5.3737 |
| sortino_ratio | -2.3192 |
| max_drawdown | 0.9088 |
| cagr | -0.6750 |
| net_avg_win | 38.0361 |
| net_avg_loss | -58.5567 |
| avg_hold_time_bars | 4.3078 |
| exposure | 0.1840 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
