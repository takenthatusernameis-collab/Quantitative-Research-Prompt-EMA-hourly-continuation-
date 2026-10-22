# EMA Hourly Continuation — BTT/USDT P34_50

**Symbol:** BTT/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 949 |
| net_profit_factor | 0.1627 |
| net_win_rate | 0.2866 |
| gross_profit_factor | 0.6270 |
| gross_win_rate | 0.3815 |
| sharpe_ratio | -16.0698 |
| sortino_ratio | -7.6312 |
| max_drawdown | 1.0000 |
| cagr | -0.9846 |
| net_avg_win | 7.1456 |
| net_avg_loss | -17.6415 |
| avg_hold_time_bars | 2.9705 |
| exposure | 0.1281 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
