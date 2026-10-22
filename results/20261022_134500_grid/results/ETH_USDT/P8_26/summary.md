# EMA Hourly Continuation — ETH/USDT P8_26

**Symbol:** ETH/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1521 |
| net_profit_factor | 0.2522 |
| net_win_rate | 0.3899 |
| gross_profit_factor | 0.8036 |
| gross_win_rate | 0.4484 |
| sharpe_ratio | -14.8955 |
| sortino_ratio | -8.2988 |
| max_drawdown | 1.0000 |
| cagr | -0.9888 |
| net_avg_win | 5.6862 |
| net_avg_loss | -14.4093 |
| avg_hold_time_bars | 3.7324 |
| exposure | 0.2580 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
