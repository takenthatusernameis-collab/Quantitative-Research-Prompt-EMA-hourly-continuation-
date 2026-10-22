# EMA Hourly Continuation — UMA/USDT P89_144

**Symbol:** UMA/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 283 |
| net_profit_factor | 0.6568 |
| net_win_rate | 0.4841 |
| gross_profit_factor | 0.9238 |
| gross_win_rate | 0.4841 |
| sharpe_ratio | -2.1918 |
| sortino_ratio | -0.5281 |
| max_drawdown | 0.4693 |
| cagr | -0.2146 |
| net_avg_win | 63.5395 |
| net_avg_loss | -90.7718 |
| avg_hold_time_bars | 9.9647 |
| exposure | 0.1282 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
