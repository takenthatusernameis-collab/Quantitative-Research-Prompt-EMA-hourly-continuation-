# EMA Hourly Continuation — XYO/USDT P89_144

**Symbol:** XYO/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 301 |
| net_profit_factor | 0.5184 |
| net_win_rate | 0.4053 |
| gross_profit_factor | 0.7344 |
| gross_win_rate | 0.4053 |
| sharpe_ratio | -3.9249 |
| sortino_ratio | -0.9676 |
| max_drawdown | 0.6846 |
| cagr | -0.3627 |
| net_avg_win | 59.9061 |
| net_avg_loss | -78.7665 |
| avg_hold_time_bars | 8.2060 |
| exposure | 0.1118 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
