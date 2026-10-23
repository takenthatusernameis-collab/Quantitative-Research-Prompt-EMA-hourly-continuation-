# EMA Hourly Continuation — IO/USDT P20_144

**Symbol:** IO/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 456 |
| net_profit_factor | 0.6141 |
| net_win_rate | 0.4539 |
| gross_profit_factor | 0.8386 |
| gross_win_rate | 0.4539 |
| sharpe_ratio | -3.5666 |
| sortino_ratio | -1.0956 |
| max_drawdown | 0.7258 |
| cagr | -0.4131 |
| net_avg_win | 54.9949 |
| net_avg_loss | -74.4486 |
| avg_hold_time_bars | 26.3662 |
| exposure | 0.5821 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
