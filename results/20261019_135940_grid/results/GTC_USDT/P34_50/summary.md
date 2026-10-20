# EMA Hourly Continuation — GTC/USDT P34_50

**Symbol:** GTC/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 892 |
| net_profit_factor | 0.4283 |
| net_win_rate | 0.4238 |
| gross_profit_factor | 0.9002 |
| gross_win_rate | 0.4417 |
| sharpe_ratio | -8.5912 |
| sortino_ratio | -3.6266 |
| max_drawdown | 0.9899 |
| cagr | -0.8376 |
| net_avg_win | 19.6147 |
| net_avg_loss | -33.6774 |
| avg_hold_time_bars | 3.3980 |
| exposure | 0.1378 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
