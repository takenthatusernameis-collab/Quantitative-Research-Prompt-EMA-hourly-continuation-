# EMA Hourly Continuation — GTC/USDT P8_144

**Symbol:** GTC/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 531 |
| net_profit_factor | 0.6659 |
| net_win_rate | 0.4689 |
| gross_profit_factor | 0.9027 |
| gross_win_rate | 0.4708 |
| sharpe_ratio | -2.9710 |
| sortino_ratio | -0.9655 |
| max_drawdown | 0.6882 |
| cagr | -0.3647 |
| net_avg_win | 54.4155 |
| net_avg_loss | -72.1599 |
| avg_hold_time_bars | 28.7872 |
| exposure | 0.6948 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
