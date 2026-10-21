# EMA Hourly Continuation — TRX/USDT P50_144

**Symbol:** TRX/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 296 |
| net_profit_factor | 0.5346 |
| net_win_rate | 0.5000 |
| gross_profit_factor | 1.0670 |
| gross_win_rate | 0.5169 |
| sharpe_ratio | -3.3198 |
| sortino_ratio | -0.8304 |
| max_drawdown | 0.6140 |
| cagr | -0.3131 |
| net_avg_win | 47.3998 |
| net_avg_loss | -88.6601 |
| avg_hold_time_bars | 16.8784 |
| exposure | 0.2271 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
