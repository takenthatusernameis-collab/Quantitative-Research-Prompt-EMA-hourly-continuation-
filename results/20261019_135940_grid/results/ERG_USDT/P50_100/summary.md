# EMA Hourly Continuation — ERG/USDT P50_100

**Symbol:** ERG/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 639 |
| net_profit_factor | 0.2787 |
| net_win_rate | 0.3584 |
| gross_profit_factor | 0.5341 |
| gross_win_rate | 0.3818 |
| sharpe_ratio | -8.3914 |
| sortino_ratio | -2.9955 |
| max_drawdown | 0.9773 |
| cagr | -0.7772 |
| net_avg_win | 16.4816 |
| net_avg_loss | -33.0343 |
| avg_hold_time_bars | 6.6698 |
| exposure | 0.1937 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
