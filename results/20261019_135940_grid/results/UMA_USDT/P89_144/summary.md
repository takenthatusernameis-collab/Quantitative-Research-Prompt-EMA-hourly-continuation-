# EMA Hourly Continuation — UMA/USDT P89_144

**Symbol:** UMA/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 488 |
| net_profit_factor | 0.4113 |
| net_win_rate | 0.4406 |
| gross_profit_factor | 0.7851 |
| gross_win_rate | 0.4631 |
| sharpe_ratio | -5.4550 |
| sortino_ratio | -1.6994 |
| max_drawdown | 0.8814 |
| cagr | -0.5694 |
| net_avg_win | 28.5783 |
| net_avg_loss | -54.7229 |
| avg_hold_time_bars | 6.5389 |
| exposure | 0.1450 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
