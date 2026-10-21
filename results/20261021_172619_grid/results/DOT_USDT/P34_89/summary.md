# EMA Hourly Continuation — DOT/USDT P34_89

**Symbol:** DOT/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 423 |
| net_profit_factor | 0.7713 |
| net_win_rate | 0.5059 |
| gross_profit_factor | 1.0092 |
| gross_win_rate | 0.5059 |
| sharpe_ratio | -1.5884 |
| sortino_ratio | -0.4692 |
| max_drawdown | 0.4395 |
| cagr | -0.1944 |
| net_avg_win | 66.0256 |
| net_avg_loss | -87.6468 |
| avg_hold_time_bars | 10.7139 |
| exposure | 0.2060 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
