# EMA Hourly Continuation — SEI/USDT P144_200

**Symbol:** SEI/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 371 |
| net_profit_factor | 0.5273 |
| net_win_rate | 0.4798 |
| gross_profit_factor | 0.9272 |
| gross_win_rate | 0.4906 |
| sharpe_ratio | -3.6870 |
| sortino_ratio | -0.9969 |
| max_drawdown | 0.7150 |
| cagr | -0.3865 |
| net_avg_win | 44.2978 |
| net_avg_loss | -77.4780 |
| avg_hold_time_bars | 4.5364 |
| exposure | 0.0765 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
