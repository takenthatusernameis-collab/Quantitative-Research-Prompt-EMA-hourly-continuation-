# EMA Hourly Continuation — AKT/USDT P12_144

**Symbol:** AKT/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 384 |
| net_profit_factor | 0.9481 |
| net_win_rate | 0.5260 |
| gross_profit_factor | 1.1009 |
| gross_win_rate | 0.5260 |
| sharpe_ratio | -0.2843 |
| sortino_ratio | -0.0803 |
| max_drawdown | 0.1747 |
| cagr | -0.0420 |
| net_avg_win | 92.4652 |
| net_avg_loss | -108.2413 |
| avg_hold_time_bars | 35.9245 |
| exposure | 0.6270 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
