# EMA Hourly Continuation — BDX/USDT P89_144

**Symbol:** BDX/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 988 |
| net_profit_factor | 0.1599 |
| net_win_rate | 0.2470 |
| gross_profit_factor | 0.4876 |
| gross_win_rate | 0.3229 |
| sharpe_ratio | -17.1452 |
| sortino_ratio | -8.2692 |
| max_drawdown | 1.0000 |
| cagr | -0.9905 |
| net_avg_win | 7.8003 |
| net_avg_loss | -15.9989 |
| avg_hold_time_bars | 2.8917 |
| exposure | 0.1299 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
