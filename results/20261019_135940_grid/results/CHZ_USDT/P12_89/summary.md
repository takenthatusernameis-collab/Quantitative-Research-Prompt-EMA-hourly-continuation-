# EMA Hourly Continuation — CHZ/USDT P12_89

**Symbol:** CHZ/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 702 |
| net_profit_factor | 0.6443 |
| net_win_rate | 0.4943 |
| gross_profit_factor | 1.0139 |
| gross_win_rate | 0.5043 |
| sharpe_ratio | -3.6223 |
| sortino_ratio | -1.3392 |
| max_drawdown | 0.8143 |
| cagr | -0.4808 |
| net_avg_win | 42.1313 |
| net_avg_loss | -63.9194 |
| avg_hold_time_bars | 16.7678 |
| exposure | 0.5350 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
