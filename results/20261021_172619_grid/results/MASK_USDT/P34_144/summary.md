# EMA Hourly Continuation — MASK/USDT P34_144

**Symbol:** MASK/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 401 |
| net_profit_factor | 0.6232 |
| net_win_rate | 0.4713 |
| gross_profit_factor | 0.8605 |
| gross_win_rate | 0.4738 |
| sharpe_ratio | -2.6847 |
| sortino_ratio | -0.7602 |
| max_drawdown | 0.6046 |
| cagr | -0.3000 |
| net_avg_win | 51.7769 |
| net_avg_loss | -74.0720 |
| avg_hold_time_bars | 21.3042 |
| exposure | 0.3883 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
