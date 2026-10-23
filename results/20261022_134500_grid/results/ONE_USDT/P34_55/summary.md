# EMA Hourly Continuation — ONE/USDT P34_55

**Symbol:** ONE/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 966 |
| net_profit_factor | 0.5088 |
| net_win_rate | 0.4172 |
| gross_profit_factor | 0.9490 |
| gross_win_rate | 0.4369 |
| sharpe_ratio | -8.8194 |
| sortino_ratio | -3.8816 |
| max_drawdown | 0.9924 |
| cagr | -0.8547 |
| net_avg_win | 25.5026 |
| net_avg_loss | -35.8771 |
| avg_hold_time_bars | 2.8075 |
| exposure | 0.1233 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
