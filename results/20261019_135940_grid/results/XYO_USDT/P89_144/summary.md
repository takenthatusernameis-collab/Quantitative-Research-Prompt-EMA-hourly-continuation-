# EMA Hourly Continuation — XYO/USDT P89_144

**Symbol:** XYO/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 624 |
| net_profit_factor | 0.3850 |
| net_win_rate | 0.3734 |
| gross_profit_factor | 0.7086 |
| gross_win_rate | 0.3862 |
| sharpe_ratio | -8.3259 |
| sortino_ratio | -2.9626 |
| max_drawdown | 0.9766 |
| cagr | -0.7727 |
| net_avg_win | 26.2245 |
| net_avg_loss | -40.5934 |
| avg_hold_time_bars | 5.0529 |
| exposure | 0.1427 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
