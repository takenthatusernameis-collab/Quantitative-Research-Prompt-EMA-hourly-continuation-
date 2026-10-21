# EMA Hourly Continuation — MNT/USDT P34_144

**Symbol:** MNT/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 298 |
| net_profit_factor | 0.8138 |
| net_win_rate | 0.5168 |
| gross_profit_factor | 1.0420 |
| gross_win_rate | 0.5168 |
| sharpe_ratio | -0.9690 |
| sortino_ratio | -0.2402 |
| max_drawdown | 0.3349 |
| cagr | -0.1063 |
| net_avg_win | 69.7640 |
| net_avg_loss | -91.6834 |
| avg_hold_time_bars | 31.5336 |
| exposure | 0.4271 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
