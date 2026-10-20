# EMA Hourly Continuation — XAI/USDT P12_89

**Symbol:** XAI/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 716 |
| net_profit_factor | 0.6700 |
| net_win_rate | 0.4581 |
| gross_profit_factor | 0.9228 |
| gross_win_rate | 0.4623 |
| sharpe_ratio | -4.3151 |
| sortino_ratio | -1.6182 |
| max_drawdown | 0.8756 |
| cagr | -0.5399 |
| net_avg_win | 53.0883 |
| net_avg_loss | -66.9843 |
| avg_hold_time_bars | 17.9134 |
| exposure | 0.5830 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
