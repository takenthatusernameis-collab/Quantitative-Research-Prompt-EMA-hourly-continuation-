# EMA Hourly Continuation — VR/USDT P8_89

**Symbol:** VR/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 483 |
| net_profit_factor | 0.8107 |
| net_win_rate | 0.4969 |
| gross_profit_factor | 0.9721 |
| gross_win_rate | 0.4969 |
| sharpe_ratio | -1.3528 |
| sortino_ratio | -0.4246 |
| max_drawdown | 0.4046 |
| cagr | -0.1805 |
| net_avg_win | 70.1918 |
| net_avg_loss | -85.5139 |
| avg_hold_time_bars | 25.5383 |
| exposure | 0.5607 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
