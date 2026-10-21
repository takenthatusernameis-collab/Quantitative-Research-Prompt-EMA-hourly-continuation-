# EMA Hourly Continuation — ETH/USDT P12_89

**Symbol:** ETH/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 410 |
| net_profit_factor | 0.7734 |
| net_win_rate | 0.5171 |
| gross_profit_factor | 1.0604 |
| gross_win_rate | 0.5171 |
| sharpe_ratio | -1.5846 |
| sortino_ratio | -0.4610 |
| max_drawdown | 0.4329 |
| cagr | -0.1913 |
| net_avg_win | 66.5169 |
| net_avg_loss | -92.0927 |
| avg_hold_time_bars | 28.8805 |
| exposure | 0.5382 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
