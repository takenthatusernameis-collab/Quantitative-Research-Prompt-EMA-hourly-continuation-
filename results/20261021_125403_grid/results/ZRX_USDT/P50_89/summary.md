# EMA Hourly Continuation — ZRX/USDT P50_89

**Symbol:** ZRX/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 428 |
| net_profit_factor | 0.6308 |
| net_win_rate | 0.4766 |
| gross_profit_factor | 0.9008 |
| gross_win_rate | 0.4766 |
| sharpe_ratio | -3.0308 |
| sortino_ratio | -0.8966 |
| max_drawdown | 0.6637 |
| cagr | -0.3373 |
| net_avg_win | 53.9568 |
| net_avg_loss | -77.8942 |
| avg_hold_time_bars | 6.9930 |
| exposure | 0.1360 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
