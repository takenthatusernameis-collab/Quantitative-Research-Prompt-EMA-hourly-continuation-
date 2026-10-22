# EMA Hourly Continuation — FLR/USDT P20_144

**Symbol:** FLR/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 679 |
| net_profit_factor | 0.4987 |
| net_win_rate | 0.4404 |
| gross_profit_factor | 0.8155 |
| gross_win_rate | 0.4536 |
| sharpe_ratio | -5.6093 |
| sortino_ratio | -2.0408 |
| max_drawdown | 0.9212 |
| cagr | -0.6341 |
| net_avg_win | 30.6122 |
| net_avg_loss | -48.2950 |
| avg_hold_time_bars | 15.9175 |
| exposure | 0.4913 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
