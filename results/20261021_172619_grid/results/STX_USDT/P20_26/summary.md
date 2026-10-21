# EMA Hourly Continuation — STX/USDT P20_26

**Symbol:** STX/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 178 |
| net_profit_factor | 0.7343 |
| net_win_rate | 0.5112 |
| gross_profit_factor | 1.0275 |
| gross_win_rate | 0.5112 |
| sharpe_ratio | -1.2280 |
| sortino_ratio | -0.2354 |
| max_drawdown | 0.3067 |
| cagr | -0.1019 |
| net_avg_win | 72.1035 |
| net_avg_loss | -102.7143 |
| avg_hold_time_bars | 5.3483 |
| exposure | 0.0431 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
