# EMA Hourly Continuation — XAI/USDT P55_100

**Symbol:** XAI/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 657 |
| net_profit_factor | 0.5885 |
| net_win_rate | 0.4658 |
| gross_profit_factor | 0.9136 |
| gross_win_rate | 0.4764 |
| sharpe_ratio | -4.6975 |
| sortino_ratio | -1.7042 |
| max_drawdown | 0.8765 |
| cagr | -0.5543 |
| net_avg_win | 40.5992 |
| net_avg_loss | -60.1399 |
| avg_hold_time_bars | 5.8721 |
| exposure | 0.1754 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
