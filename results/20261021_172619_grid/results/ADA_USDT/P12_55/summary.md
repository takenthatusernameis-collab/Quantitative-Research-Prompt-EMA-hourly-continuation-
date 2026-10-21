# EMA Hourly Continuation — ADA/USDT P12_55

**Symbol:** ADA/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 591 |
| net_profit_factor | 0.7307 |
| net_win_rate | 0.4907 |
| gross_profit_factor | 0.9550 |
| gross_win_rate | 0.4907 |
| sharpe_ratio | -2.3265 |
| sortino_ratio | -0.8094 |
| max_drawdown | 0.6192 |
| cagr | -0.3102 |
| net_avg_win | 56.7452 |
| net_avg_loss | -74.8216 |
| avg_hold_time_bars | 12.4501 |
| exposure | 0.3345 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
