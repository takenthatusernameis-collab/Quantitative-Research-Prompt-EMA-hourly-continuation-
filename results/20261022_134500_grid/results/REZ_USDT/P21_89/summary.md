# EMA Hourly Continuation — REZ/USDT P21_89

**Symbol:** REZ/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 674 |
| net_profit_factor | 0.7307 |
| net_win_rate | 0.4955 |
| gross_profit_factor | 0.9961 |
| gross_win_rate | 0.5015 |
| sharpe_ratio | -2.6125 |
| sortino_ratio | -0.9709 |
| max_drawdown | 0.7067 |
| cagr | -0.3666 |
| net_avg_win | 54.9896 |
| net_avg_loss | -73.9284 |
| avg_hold_time_bars | 12.6499 |
| exposure | 0.3934 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
