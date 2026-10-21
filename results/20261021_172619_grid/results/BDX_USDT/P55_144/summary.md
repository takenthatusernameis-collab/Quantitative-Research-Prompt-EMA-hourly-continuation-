# EMA Hourly Continuation — BDX/USDT P55_144

**Symbol:** BDX/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 326 |
| net_profit_factor | 0.4648 |
| net_win_rate | 0.4356 |
| gross_profit_factor | 0.7654 |
| gross_win_rate | 0.4387 |
| sharpe_ratio | -4.0518 |
| sortino_ratio | -1.0484 |
| max_drawdown | 0.7068 |
| cagr | -0.3834 |
| net_avg_win | 43.0026 |
| net_avg_loss | -71.3993 |
| avg_hold_time_bars | 11.4264 |
| exposure | 0.1693 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
