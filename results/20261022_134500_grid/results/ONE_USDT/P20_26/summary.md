# EMA Hourly Continuation — ONE/USDT P20_26

**Symbol:** ONE/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1262 |
| net_profit_factor | 0.2845 |
| net_win_rate | 0.3843 |
| gross_profit_factor | 0.7821 |
| gross_win_rate | 0.4081 |
| sharpe_ratio | -13.7178 |
| sortino_ratio | -7.0036 |
| max_drawdown | 0.9999 |
| cagr | -0.9763 |
| net_avg_win | 8.1986 |
| net_avg_loss | -17.9865 |
| avg_hold_time_bars | 1.8265 |
| exposure | 0.1048 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
