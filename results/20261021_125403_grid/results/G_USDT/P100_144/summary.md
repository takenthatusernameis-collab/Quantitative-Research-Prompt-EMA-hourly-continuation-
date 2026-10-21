# EMA Hourly Continuation — G/USDT P100_144

**Symbol:** G/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 230 |
| net_profit_factor | 0.5571 |
| net_win_rate | 0.4696 |
| gross_profit_factor | 0.8512 |
| gross_win_rate | 0.4696 |
| sharpe_ratio | -2.7327 |
| sortino_ratio | -0.6394 |
| max_drawdown | 0.4911 |
| cagr | -0.2529 |
| net_avg_win | 54.6201 |
| net_avg_loss | -86.7911 |
| avg_hold_time_bars | 6.8957 |
| exposure | 0.0834 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
