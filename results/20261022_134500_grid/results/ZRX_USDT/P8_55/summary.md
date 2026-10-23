# EMA Hourly Continuation — ZRX/USDT P8_55

**Symbol:** ZRX/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1015 |
| net_profit_factor | 0.5250 |
| net_win_rate | 0.4493 |
| gross_profit_factor | 0.8372 |
| gross_win_rate | 0.4631 |
| sharpe_ratio | -6.2660 |
| sortino_ratio | -2.8004 |
| max_drawdown | 0.9686 |
| cagr | -0.7414 |
| net_avg_win | 23.4220 |
| net_avg_loss | -36.3961 |
| avg_hold_time_bars | 10.9813 |
| exposure | 0.5066 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
