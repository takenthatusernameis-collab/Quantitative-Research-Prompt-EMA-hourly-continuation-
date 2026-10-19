# EMA Hourly Continuation — TRX/USDT P8_144

**Symbol:** TRX/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 562 |
| net_profit_factor | 0.3981 |
| net_win_rate | 0.4110 |
| gross_profit_factor | 0.9006 |
| gross_win_rate | 0.4733 |
| sharpe_ratio | -7.3434 |
| sortino_ratio | -2.4304 |
| max_drawdown | 0.9631 |
| cagr | -0.7260 |
| net_avg_win | 27.5249 |
| net_avg_loss | -48.2512 |
| avg_hold_time_bars | 27.4377 |
| exposure | 0.7009 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
