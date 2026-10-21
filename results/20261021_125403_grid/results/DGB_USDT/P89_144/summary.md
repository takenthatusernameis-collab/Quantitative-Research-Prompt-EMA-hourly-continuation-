# EMA Hourly Continuation — DGB/USDT P89_144

**Symbol:** DGB/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 268 |
| net_profit_factor | 0.6311 |
| net_win_rate | 0.4515 |
| gross_profit_factor | 0.8421 |
| gross_win_rate | 0.4515 |
| sharpe_ratio | -2.4604 |
| sortino_ratio | -0.5736 |
| max_drawdown | 0.4932 |
| cagr | -0.2317 |
| net_avg_win | 68.4642 |
| net_avg_loss | -89.2919 |
| avg_hold_time_bars | 7.8955 |
| exposure | 0.0962 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
