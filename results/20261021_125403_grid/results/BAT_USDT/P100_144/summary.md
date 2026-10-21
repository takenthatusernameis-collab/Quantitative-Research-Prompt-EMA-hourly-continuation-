# EMA Hourly Continuation — BAT/USDT P100_144

**Symbol:** BAT/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 271 |
| net_profit_factor | 0.6598 |
| net_win_rate | 0.4834 |
| gross_profit_factor | 0.9554 |
| gross_win_rate | 0.4834 |
| sharpe_ratio | -2.2162 |
| sortino_ratio | -0.5233 |
| max_drawdown | 0.4712 |
| cagr | -0.2126 |
| net_avg_win | 66.8383 |
| net_avg_loss | -94.7835 |
| avg_hold_time_bars | 6.3432 |
| exposure | 0.0781 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
