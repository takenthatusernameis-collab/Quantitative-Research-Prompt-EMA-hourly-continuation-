# EMA Hourly Continuation — TIA/USDT P34_200

**Symbol:** TIA/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 322 |
| net_profit_factor | 0.7978 |
| net_win_rate | 0.5062 |
| gross_profit_factor | 1.0193 |
| gross_win_rate | 0.5062 |
| sharpe_ratio | -1.2276 |
| sortino_ratio | -0.3142 |
| max_drawdown | 0.3340 |
| cagr | -0.1367 |
| net_avg_win | 74.6894 |
| net_avg_loss | -95.9773 |
| avg_hold_time_bars | 36.6770 |
| exposure | 0.5368 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
