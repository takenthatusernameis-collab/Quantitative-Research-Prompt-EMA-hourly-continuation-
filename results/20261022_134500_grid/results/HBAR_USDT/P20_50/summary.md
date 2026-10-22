# EMA Hourly Continuation — HBAR/USDT P20_50

**Symbol:** HBAR/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 968 |
| net_profit_factor | 0.4548 |
| net_win_rate | 0.4566 |
| gross_profit_factor | 0.8661 |
| gross_win_rate | 0.4721 |
| sharpe_ratio | -7.7691 |
| sortino_ratio | -3.3978 |
| max_drawdown | 0.9862 |
| cagr | -0.8185 |
| net_avg_win | 18.6151 |
| net_avg_loss | -34.3919 |
| avg_hold_time_bars | 4.6973 |
| exposure | 0.2067 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
