# EMA Hourly Continuation — SEI/USDT P8_89

**Symbol:** SEI/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 442 |
| net_profit_factor | 0.9246 |
| net_win_rate | 0.5226 |
| gross_profit_factor | 1.0940 |
| gross_win_rate | 0.5226 |
| sharpe_ratio | -0.4998 |
| sortino_ratio | -0.1514 |
| max_drawdown | 0.2715 |
| cagr | -0.0724 |
| net_avg_win | 91.2925 |
| net_avg_loss | -108.0949 |
| avg_hold_time_bars | 33.1674 |
| exposure | 0.6664 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
