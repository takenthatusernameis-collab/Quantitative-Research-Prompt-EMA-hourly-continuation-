# EMA Hourly Continuation — G/USDT P34_50

**Symbol:** G/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 367 |
| net_profit_factor | 0.5880 |
| net_win_rate | 0.4796 |
| gross_profit_factor | 0.9274 |
| gross_win_rate | 0.4796 |
| sharpe_ratio | -3.4071 |
| sortino_ratio | -1.0098 |
| max_drawdown | 0.6324 |
| cagr | -0.3679 |
| net_avg_win | 51.1337 |
| net_avg_loss | -80.1345 |
| avg_hold_time_bars | 6.0926 |
| exposure | 0.1176 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
