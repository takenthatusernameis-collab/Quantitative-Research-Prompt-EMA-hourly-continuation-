# EMA Hourly Continuation — BCH/USDT P100_144

**Symbol:** BCH/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 217 |
| net_profit_factor | 0.6255 |
| net_win_rate | 0.4793 |
| gross_profit_factor | 0.9296 |
| gross_win_rate | 0.4793 |
| sharpe_ratio | -2.2107 |
| sortino_ratio | -0.4676 |
| max_drawdown | 0.4416 |
| cagr | -0.1925 |
| net_avg_win | 66.7321 |
| net_avg_loss | -98.1891 |
| avg_hold_time_bars | 6.5991 |
| exposure | 0.0651 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
