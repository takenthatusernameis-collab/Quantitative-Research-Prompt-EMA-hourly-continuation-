# EMA Hourly Continuation — DGB/USDT P34_200

**Symbol:** DGB/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 335 |
| net_profit_factor | 0.6908 |
| net_win_rate | 0.4567 |
| gross_profit_factor | 0.8361 |
| gross_win_rate | 0.4567 |
| sharpe_ratio | -2.1151 |
| sortino_ratio | -0.5491 |
| max_drawdown | 0.5051 |
| cagr | -0.2243 |
| net_avg_win | 68.8579 |
| net_avg_loss | -83.7993 |
| avg_hold_time_bars | 32.7075 |
| exposure | 0.4980 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
