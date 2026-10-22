# EMA Hourly Continuation — JTO/USDT P26_144

**Symbol:** JTO/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 524 |
| net_profit_factor | 0.6909 |
| net_win_rate | 0.4637 |
| gross_profit_factor | 0.9108 |
| gross_win_rate | 0.4656 |
| sharpe_ratio | -2.9167 |
| sortino_ratio | -0.9432 |
| max_drawdown | 0.6851 |
| cagr | -0.3567 |
| net_avg_win | 61.6077 |
| net_avg_loss | -77.1081 |
| avg_hold_time_bars | 18.6832 |
| exposure | 0.4450 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
