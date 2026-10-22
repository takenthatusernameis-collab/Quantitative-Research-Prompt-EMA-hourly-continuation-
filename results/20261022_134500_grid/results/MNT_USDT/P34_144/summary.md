# EMA Hourly Continuation — MNT/USDT P34_144

**Symbol:** MNT/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 394 |
| net_profit_factor | 0.4681 |
| net_win_rate | 0.4518 |
| gross_profit_factor | 0.7938 |
| gross_win_rate | 0.4695 |
| sharpe_ratio | -3.7793 |
| sortino_ratio | -1.0464 |
| max_drawdown | 0.7451 |
| cagr | -0.4061 |
| net_avg_win | 36.0810 |
| net_avg_loss | -63.5173 |
| avg_hold_time_bars | 24.2107 |
| exposure | 0.4336 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
