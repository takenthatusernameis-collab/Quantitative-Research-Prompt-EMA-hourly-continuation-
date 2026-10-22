# EMA Hourly Continuation — GMT/USDT P20_144

**Symbol:** GMT/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 383 |
| net_profit_factor | 0.6813 |
| net_win_rate | 0.4517 |
| gross_profit_factor | 0.8317 |
| gross_win_rate | 0.4517 |
| sharpe_ratio | -2.4046 |
| sortino_ratio | -0.6672 |
| max_drawdown | 0.5742 |
| cagr | -0.2648 |
| net_avg_win | 66.4876 |
| net_avg_loss | -80.3996 |
| avg_hold_time_bars | 28.2689 |
| exposure | 0.4921 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
