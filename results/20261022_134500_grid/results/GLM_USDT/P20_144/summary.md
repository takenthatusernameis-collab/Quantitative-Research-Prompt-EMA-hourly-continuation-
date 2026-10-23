# EMA Hourly Continuation — GLM/USDT P20_144

**Symbol:** GLM/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 509 |
| net_profit_factor | 0.6109 |
| net_win_rate | 0.4656 |
| gross_profit_factor | 0.9016 |
| gross_win_rate | 0.4735 |
| sharpe_ratio | -3.5105 |
| sortino_ratio | -1.1130 |
| max_drawdown | 0.7398 |
| cagr | -0.4118 |
| net_avg_win | 48.7861 |
| net_avg_loss | -69.5780 |
| avg_hold_time_bars | 24.4244 |
| exposure | 0.5651 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
