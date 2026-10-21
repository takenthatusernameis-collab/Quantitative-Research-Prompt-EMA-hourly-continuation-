# EMA Hourly Continuation — ZEN/USDT P12_26

**Symbol:** ZEN/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 498 |
| net_profit_factor | 0.6426 |
| net_win_rate | 0.4739 |
| gross_profit_factor | 0.9087 |
| gross_win_rate | 0.4739 |
| sharpe_ratio | -3.0955 |
| sortino_ratio | -0.9880 |
| max_drawdown | 0.6802 |
| cagr | -0.3637 |
| net_avg_win | 51.7101 |
| net_avg_loss | -72.4822 |
| avg_hold_time_bars | 5.5723 |
| exposure | 0.1261 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
