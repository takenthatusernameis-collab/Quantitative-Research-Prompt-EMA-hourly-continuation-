# EMA Hourly Continuation — WOO/USDT P20_144

**Symbol:** WOO/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 471 |
| net_profit_factor | 0.7113 |
| net_win_rate | 0.4798 |
| gross_profit_factor | 0.9628 |
| gross_win_rate | 0.4862 |
| sharpe_ratio | -2.5202 |
| sortino_ratio | -0.7713 |
| max_drawdown | 0.6097 |
| cagr | -0.3046 |
| net_avg_win | 65.2435 |
| net_avg_loss | -84.6063 |
| avg_hold_time_bars | 26.1083 |
| exposure | 0.5590 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
