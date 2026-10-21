# EMA Hourly Continuation — CTC/USDT P34_89

**Symbol:** CTC/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 443 |
| net_profit_factor | 0.7105 |
| net_win_rate | 0.4966 |
| gross_profit_factor | 0.9902 |
| gross_win_rate | 0.4966 |
| sharpe_ratio | -2.3030 |
| sortino_ratio | -0.6945 |
| max_drawdown | 0.5824 |
| cagr | -0.2738 |
| net_avg_win | 61.5882 |
| net_avg_loss | -85.5195 |
| avg_hold_time_bars | 10.9007 |
| exposure | 0.2195 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
