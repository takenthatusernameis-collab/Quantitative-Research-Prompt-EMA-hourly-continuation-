# EMA Hourly Continuation — STX/USDT P12_50

**Symbol:** STX/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 643 |
| net_profit_factor | 0.7358 |
| net_win_rate | 0.4930 |
| gross_profit_factor | 0.9435 |
| gross_win_rate | 0.4930 |
| sharpe_ratio | -2.2856 |
| sortino_ratio | -0.8276 |
| max_drawdown | 0.6388 |
| cagr | -0.3156 |
| net_avg_win | 54.1150 |
| net_avg_loss | -71.5125 |
| avg_hold_time_bars | 11.3048 |
| exposure | 0.3289 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
