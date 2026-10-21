# EMA Hourly Continuation — TAO/USDT P20_21

**Symbol:** TAO/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 86 |
| net_profit_factor | 0.6917 |
| net_win_rate | 0.4651 |
| gross_profit_factor | 0.8849 |
| gross_win_rate | 0.4651 |
| sharpe_ratio | -1.1305 |
| sortino_ratio | -0.1494 |
| max_drawdown | 0.2502 |
| cagr | -0.0668 |
| net_avg_win | 89.3711 |
| net_avg_loss | -112.3486 |
| avg_hold_time_bars | 4.9767 |
| exposure | 0.0195 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
