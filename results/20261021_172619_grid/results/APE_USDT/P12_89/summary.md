# EMA Hourly Continuation — APE/USDT P12_89

**Symbol:** APE/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 537 |
| net_profit_factor | 0.7512 |
| net_win_rate | 0.4767 |
| gross_profit_factor | 0.9275 |
| gross_win_rate | 0.4767 |
| sharpe_ratio | -2.2307 |
| sortino_ratio | -0.7367 |
| max_drawdown | 0.5892 |
| cagr | -0.2873 |
| net_avg_win | 67.5620 |
| net_avg_loss | -81.9368 |
| avg_hold_time_bars | 21.3371 |
| exposure | 0.5208 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
