# EMA Hourly Continuation — METIS/USDT P89_144

**Symbol:** METIS/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 520 |
| net_profit_factor | 0.5191 |
| net_win_rate | 0.4423 |
| gross_profit_factor | 0.8575 |
| gross_win_rate | 0.4500 |
| sharpe_ratio | -4.9524 |
| sortino_ratio | -1.6071 |
| max_drawdown | 0.8539 |
| cagr | -0.5323 |
| net_avg_win | 39.9716 |
| net_avg_loss | -61.0709 |
| avg_hold_time_bars | 5.4192 |
| exposure | 0.1281 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
