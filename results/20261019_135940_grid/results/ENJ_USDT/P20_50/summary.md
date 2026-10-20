# EMA Hourly Continuation — ENJ/USDT P20_50

**Symbol:** ENJ/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1010 |
| net_profit_factor | 0.5028 |
| net_win_rate | 0.4535 |
| gross_profit_factor | 0.9460 |
| gross_win_rate | 0.4673 |
| sharpe_ratio | -7.4923 |
| sortino_ratio | -3.3607 |
| max_drawdown | 0.9846 |
| cagr | -0.8080 |
| net_avg_win | 21.7273 |
| net_avg_loss | -35.8559 |
| avg_hold_time_bars | 4.3505 |
| exposure | 0.1997 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
