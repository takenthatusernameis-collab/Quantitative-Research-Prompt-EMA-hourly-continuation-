# EMA Hourly Continuation — LISTA/USDT P12_21

**Symbol:** LISTA/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1196 |
| net_profit_factor | 0.4992 |
| net_win_rate | 0.4231 |
| gross_profit_factor | 0.9565 |
| gross_win_rate | 0.4565 |
| sharpe_ratio | -9.9294 |
| sortino_ratio | -5.0446 |
| max_drawdown | 0.9972 |
| cagr | -0.9176 |
| net_avg_win | 19.6380 |
| net_avg_loss | -28.8512 |
| avg_hold_time_bars | 3.3286 |
| exposure | 0.1947 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
