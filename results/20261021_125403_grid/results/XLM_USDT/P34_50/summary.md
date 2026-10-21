# EMA Hourly Continuation — XLM/USDT P34_50

**Symbol:** XLM/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 211 |
| net_profit_factor | 0.7184 |
| net_win_rate | 0.5355 |
| gross_profit_factor | 1.1269 |
| gross_win_rate | 0.5355 |
| sharpe_ratio | -1.3447 |
| sortino_ratio | -0.2828 |
| max_drawdown | 0.2932 |
| cagr | -0.1205 |
| net_avg_win | 62.2574 |
| net_avg_loss | -99.9190 |
| avg_hold_time_bars | 6.0806 |
| exposure | 0.0583 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
