# EMA Hourly Continuation — COTI/USDT P55_89

**Symbol:** COTI/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 727 |
| net_profit_factor | 0.4732 |
| net_win_rate | 0.4567 |
| gross_profit_factor | 0.8012 |
| gross_win_rate | 0.4635 |
| sharpe_ratio | -5.7670 |
| sortino_ratio | -2.2058 |
| max_drawdown | 0.9307 |
| cagr | -0.6546 |
| net_avg_win | 25.1824 |
| net_avg_loss | -44.7288 |
| avg_hold_time_bars | 3.6052 |
| exposure | 0.1191 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
