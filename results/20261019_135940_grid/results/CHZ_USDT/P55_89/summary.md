# EMA Hourly Continuation — CHZ/USDT P55_89

**Symbol:** CHZ/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 643 |
| net_profit_factor | 0.4871 |
| net_win_rate | 0.4852 |
| gross_profit_factor | 1.0603 |
| gross_win_rate | 0.5117 |
| sharpe_ratio | -5.5563 |
| sortino_ratio | -1.9846 |
| max_drawdown | 0.9188 |
| cagr | -0.6268 |
| net_avg_win | 27.8779 |
| net_avg_loss | -53.9466 |
| avg_hold_time_bars | 3.9098 |
| exposure | 0.1143 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
