# EMA Hourly Continuation — LUNC/USDT P34_200

**Symbol:** LUNC/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 334 |
| net_profit_factor | 0.7180 |
| net_win_rate | 0.4820 |
| gross_profit_factor | 0.9089 |
| gross_win_rate | 0.4820 |
| sharpe_ratio | -1.7909 |
| sortino_ratio | -0.4662 |
| max_drawdown | 0.4404 |
| cagr | -0.1935 |
| net_avg_win | 65.9740 |
| net_avg_loss | -85.5144 |
| avg_hold_time_bars | 30.3772 |
| exposure | 0.4612 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
