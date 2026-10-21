# EMA Hourly Continuation — ENA/USDT P34_144

**Symbol:** ENA/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 333 |
| net_profit_factor | 0.9014 |
| net_win_rate | 0.5105 |
| gross_profit_factor | 1.0312 |
| gross_win_rate | 0.5135 |
| sharpe_ratio | -0.5037 |
| sortino_ratio | -0.1318 |
| max_drawdown | 0.3267 |
| cagr | -0.0625 |
| net_avg_win | 80.3973 |
| net_avg_loss | -93.0252 |
| avg_hold_time_bars | 24.0090 |
| exposure | 0.3634 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
