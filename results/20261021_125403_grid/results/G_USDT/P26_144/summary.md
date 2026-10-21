# EMA Hourly Continuation — G/USDT P26_144

**Symbol:** G/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 328 |
| net_profit_factor | 0.6332 |
| net_win_rate | 0.4421 |
| gross_profit_factor | 0.7912 |
| gross_win_rate | 0.4421 |
| sharpe_ratio | -2.7990 |
| sortino_ratio | -0.7723 |
| max_drawdown | 0.5834 |
| cagr | -0.3000 |
| net_avg_win | 64.1706 |
| net_avg_loss | -80.2978 |
| avg_hold_time_bars | 29.3841 |
| exposure | 0.5068 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
