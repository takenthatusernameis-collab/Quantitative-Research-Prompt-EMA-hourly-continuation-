# EMA Hourly Continuation — RIO/USDT P34_144

**Symbol:** RIO/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 372 |
| net_profit_factor | 0.7214 |
| net_win_rate | 0.4489 |
| gross_profit_factor | 0.8125 |
| gross_win_rate | 0.4489 |
| sharpe_ratio | -2.0169 |
| sortino_ratio | -0.5520 |
| max_drawdown | 0.5063 |
| cagr | -0.2255 |
| net_avg_win | 72.9322 |
| net_avg_loss | -82.3567 |
| avg_hold_time_bars | 20.7527 |
| exposure | 0.3544 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
