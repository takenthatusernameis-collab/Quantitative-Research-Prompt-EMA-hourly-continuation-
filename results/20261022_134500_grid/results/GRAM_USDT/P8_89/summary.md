# EMA Hourly Continuation — GRAM/USDT P8_89

**Symbol:** GRAM/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 759 |
| net_profit_factor | 0.4899 |
| net_win_rate | 0.4717 |
| gross_profit_factor | 0.9007 |
| gross_win_rate | 0.4822 |
| sharpe_ratio | -5.4905 |
| sortino_ratio | -2.0961 |
| max_drawdown | 0.9346 |
| cagr | -0.6515 |
| net_avg_win | 24.9281 |
| net_avg_loss | -45.4261 |
| avg_hold_time_bars | 18.2727 |
| exposure | 0.6304 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
