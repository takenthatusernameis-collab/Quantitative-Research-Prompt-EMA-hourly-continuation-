# EMA Hourly Continuation — XDC/USDT P50_89

**Symbol:** XDC/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 321 |
| net_profit_factor | 0.6749 |
| net_win_rate | 0.5202 |
| gross_profit_factor | 1.0838 |
| gross_win_rate | 0.5202 |
| sharpe_ratio | -2.1481 |
| sortino_ratio | -0.5555 |
| max_drawdown | 0.4833 |
| cagr | -0.2236 |
| net_avg_win | 58.4868 |
| net_avg_loss | -93.9724 |
| avg_hold_time_bars | 7.2087 |
| exposure | 0.1052 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
