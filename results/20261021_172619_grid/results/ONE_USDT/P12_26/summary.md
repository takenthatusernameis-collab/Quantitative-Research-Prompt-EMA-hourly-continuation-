# EMA Hourly Continuation — ONE/USDT P12_26

**Symbol:** ONE/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 438 |
| net_profit_factor | 0.7637 |
| net_win_rate | 0.5068 |
| gross_profit_factor | 1.0193 |
| gross_win_rate | 0.5091 |
| sharpe_ratio | -1.6753 |
| sortino_ratio | -0.5039 |
| max_drawdown | 0.4979 |
| cagr | -0.2063 |
| net_avg_win | 64.0629 |
| net_avg_loss | -86.2201 |
| avg_hold_time_bars | 5.1119 |
| exposure | 0.1018 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
