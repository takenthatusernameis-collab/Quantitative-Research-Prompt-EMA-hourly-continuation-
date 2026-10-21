# EMA Hourly Continuation — CFG/USDT P26_34

**Symbol:** CFG/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 144 |
| net_profit_factor | 0.4920 |
| net_win_rate | 0.4097 |
| gross_profit_factor | 0.6736 |
| gross_win_rate | 0.4097 |
| sharpe_ratio | -2.4750 |
| sortino_ratio | -0.4207 |
| max_drawdown | 0.3926 |
| cagr | -0.1771 |
| net_avg_win | 63.5306 |
| net_avg_loss | -89.6348 |
| avg_hold_time_bars | 44.3194 |
| exposure | 0.2901 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
