# EMA Hourly Continuation — BDX/USDT P50_144

**Symbol:** BDX/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 340 |
| net_profit_factor | 0.5054 |
| net_win_rate | 0.4471 |
| gross_profit_factor | 0.8242 |
| gross_win_rate | 0.4500 |
| sharpe_ratio | -3.8594 |
| sortino_ratio | -1.0200 |
| max_drawdown | 0.6966 |
| cagr | -0.3750 |
| net_avg_win | 46.5847 |
| net_avg_loss | -74.5176 |
| avg_hold_time_bars | 11.5735 |
| exposure | 0.1789 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
