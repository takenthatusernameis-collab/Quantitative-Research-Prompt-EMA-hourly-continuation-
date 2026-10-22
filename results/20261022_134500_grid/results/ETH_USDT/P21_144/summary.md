# EMA Hourly Continuation — ETH/USDT P21_144

**Symbol:** ETH/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 371 |
| net_profit_factor | 0.4735 |
| net_win_rate | 0.4609 |
| gross_profit_factor | 0.8823 |
| gross_win_rate | 0.4771 |
| sharpe_ratio | -4.2649 |
| sortino_ratio | -1.1518 |
| max_drawdown | 0.7745 |
| cagr | -0.4320 |
| net_avg_win | 39.8865 |
| net_avg_loss | -72.0255 |
| avg_hold_time_bars | 36.5283 |
| exposure | 0.6160 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
