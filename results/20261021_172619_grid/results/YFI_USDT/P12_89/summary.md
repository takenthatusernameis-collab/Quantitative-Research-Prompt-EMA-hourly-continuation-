# EMA Hourly Continuation — YFI/USDT P12_89

**Symbol:** YFI/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 556 |
| net_profit_factor | 0.7063 |
| net_win_rate | 0.4856 |
| gross_profit_factor | 0.9729 |
| gross_win_rate | 0.4856 |
| sharpe_ratio | -2.8266 |
| sortino_ratio | -0.9504 |
| max_drawdown | 0.6855 |
| cagr | -0.3542 |
| net_avg_win | 59.5084 |
| net_avg_loss | -79.5405 |
| avg_hold_time_bars | 21.1942 |
| exposure | 0.5332 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
