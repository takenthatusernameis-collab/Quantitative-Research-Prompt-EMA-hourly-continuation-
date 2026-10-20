# EMA Hourly Continuation — MEW/USDT P50_144

**Symbol:** MEW/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 484 |
| net_profit_factor | 0.6345 |
| net_win_rate | 0.4690 |
| gross_profit_factor | 0.8779 |
| gross_win_rate | 0.4731 |
| sharpe_ratio | -3.0956 |
| sortino_ratio | -0.9604 |
| max_drawdown | 0.6912 |
| cagr | -0.3654 |
| net_avg_win | 52.0578 |
| net_avg_loss | -72.4733 |
| avg_hold_time_bars | 12.6302 |
| exposure | 0.2779 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
