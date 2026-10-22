# EMA Hourly Continuation — ETH/USDT P20_34

**Symbol:** ETH/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1100 |
| net_profit_factor | 0.2158 |
| net_win_rate | 0.3418 |
| gross_profit_factor | 0.8536 |
| gross_win_rate | 0.4300 |
| sharpe_ratio | -14.7069 |
| sortino_ratio | -7.1990 |
| max_drawdown | 0.9999 |
| cagr | -0.9784 |
| net_avg_win | 7.3194 |
| net_avg_loss | -17.6125 |
| avg_hold_time_bars | 2.6464 |
| exposure | 0.1323 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
