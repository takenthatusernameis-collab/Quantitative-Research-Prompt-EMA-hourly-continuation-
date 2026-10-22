# EMA Hourly Continuation — TRADE/USDT P34_144

**Symbol:** TRADE/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 398 |
| net_profit_factor | 0.6353 |
| net_win_rate | 0.4573 |
| gross_profit_factor | 0.8692 |
| gross_win_rate | 0.4598 |
| sharpe_ratio | -2.9952 |
| sortino_ratio | -0.8337 |
| max_drawdown | 0.6729 |
| cagr | -0.3336 |
| net_avg_win | 61.1883 |
| net_avg_loss | -81.1494 |
| avg_hold_time_bars | 21.0402 |
| exposure | 0.3806 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
