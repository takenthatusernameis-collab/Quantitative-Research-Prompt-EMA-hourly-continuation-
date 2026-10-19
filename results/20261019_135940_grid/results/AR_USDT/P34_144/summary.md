# EMA Hourly Continuation — AR/USDT P34_144

**Symbol:** AR/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 474 |
| net_profit_factor | 0.6193 |
| net_win_rate | 0.4557 |
| gross_profit_factor | 0.8358 |
| gross_win_rate | 0.4662 |
| sharpe_ratio | -3.0932 |
| sortino_ratio | -0.9471 |
| max_drawdown | 0.6933 |
| cagr | -0.3617 |
| net_avg_win | 50.9169 |
| net_avg_loss | -68.8338 |
| avg_hold_time_bars | 19.2257 |
| exposure | 0.4142 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
